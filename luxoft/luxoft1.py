# pylint: disable=missing-module-docstring
#
# poweredby2dor
#
import json
# pylint: disable=missing-function-docstring


def check_order(json_input, batter_id, topping_id):
    try:
        # Parse the JSON input
        data = json.loads(json_input)

        # Check if the batter_id is valid
        batter_found = False
        for batter in data["batters"]["batter"]:
            if batter["id"] == batter_id:
                batter_found = True
                break

        if not batter_found:
            print(f"\nBatter with ID {batter_id} not found.")
            return False

        # Check if the topping_id is valid
        topping_found = False
        for topping in data["topping"]:
            if topping["id"] == topping_id:
                topping_found = True
                break

        if not topping_found:
            print(f"\nOrder cannot be completed. Topping with ID {topping_id} not found.")
            return False

        # Order can be completed if both batter and topping are valid
        print("\nOrder can be completed.")
        return True

    except json.JSONDecodeError:
        print("\nInvalid JSON response.")
        return False


# Example usage:
# pylint: disable=invalid-name
json_response = '''
{
    "batters": {
        "batter": [
            {"id":"1001","type":"Regular"},
            {"id":"1002","type":"Chocolate"},
            {"id":"1003","type":"Blueberry"},
            {"id":"1004","type":"Devi's Food"}
        ]
    },
    "topping": [
        {"id":"5001","type":"None"},
        {"id":"5002","type":"Glazed"},
        {"id":"5005","type":"Sugar"},
        {"id":"5007","type":"Powdered Sugar"},
        {"id":"5006","type":"Chocolate with Sprinkles"},
        {"id":"5003","type":"chocolate"},
        {"id":"5004","type":"Maple"}
    ]
}
'''

order1_batter_id = "1002"
order1_topping_id = "5005"
check_order(json_response, order1_batter_id, order1_topping_id)

order2_batter_id = "1010"  # Invalid batter ID
order2_topping_id = "5002"
check_order(json_response, order2_batter_id, order2_topping_id)
