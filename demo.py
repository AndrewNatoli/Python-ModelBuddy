import modelbuddy

# import modelbuddy.functions

__author__ = 'andrew'

modelbuddy.debug("debug message test")

# person = modelbuddy.get("person", {"person_id":"1"})
# person.set({"firstname":"John","lastname":"Fredrickson"})
# person.update()


new_person = modelbuddy.get("person")

new_person.set({"bacon":"fresh","firstname":"john"})
new_person.insert()


# other_person = modelbuddy.get("person","person_id=%s",("1"))
# other_person.set({"firstname:Joe"})
# other_person.update()