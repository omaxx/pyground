import yaml

from pyground import db

MODELS = {
    db.Foo: "inventory/foo.yaml",
    db.Bar: "inventory/bar.yaml",
    db.User: "inventory/users.yaml"
}

for model, file in MODELS.items():
    print(model.drop_collection())

    with open(file) as io:
        for item in yaml.safe_load(io):
            print(model.create(**item))
