# @version ^0.4.1

owner: public(address)
advice_registry: public(HashMap[address, String[500]])

@external
def __init__():
    self.owner = msg.sender

@external
def store_advice(user: address, advice: String[500]):
    assert msg.sender == self.owner, "Only owner can store advice"
    self.advice_registry[user] = advice

@external
@view
def get_advice(user: address) -> String[500]:
    return self.advice_registry[user] 