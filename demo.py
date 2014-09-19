import modelbuddy

# import modelbuddy.functions

__author__ = 'andrew'

modelbuddy.debug("debug message test")

person = modelbuddy.get("person", {"person_id":"1"})
# new_person = modelbuddy.get("person")
# other_person = modelbuddy.get("person","person_id=%s",("1"))
#
# new_person.set({"bacon":"fresh","firstname":"john"})
#
person.set({"firstname":"John","lastname":"Fredrickson"})
person.update()
#
# other_person.set({"firstname:Joe"})
# other_person.update()