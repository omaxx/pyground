import asyncio
import concurrent.futures

import urwid

from .device import Device
from . import widgets

fields = ["name", "ip", "status", "version"]
DEVICES = [
    Device("r1", "172.31.8.1", "jnpr", "Juniper#123"),
    Device("r2", "172.31.8.2", "jnpr", "Juniper#123"),
    Device("sw1", "172.31.8.3", "jnpr", "Juniper#123"),
    Device("sw2", "172.31.8.4", "jnpr", "Juniper#123"),
    Device("srx1", "172.31.8.5", "jnpr", "Juniper#123"),
    Device("srx2", "172.31.8.6", "jnpr", "Juniper#123"),
]


class TUI:
    def run(self):
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)
        self.loop = asyncio.get_event_loop()
        urwid_loop = urwid.MainLoop(
            widgets.Main(DEVICES, fields),
            event_loop=urwid.AsyncioEventLoop(loop=self.loop),
            unhandled_input=self.unhandled,
        )
        urwid_loop.set_alarm_in(0, refresh, user_data={})
        urwid_loop.run()
        print(DEVICES)

    def unhandled(self, key):
        if key in ('u',):
            self.loop.create_task(self.fetch_data())
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()
        if key == 'ctrl c':
            raise urwid.ExitMainLoop

    async def fetch_data(self):
        for device in DEVICES:
            self.loop.run_in_executor(self.executor, device.update)


def refresh(loop, data):
    loop.draw_screen()
    loop.set_alarm_in(1, refresh)
