class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0

        for bill in bills:
            if bill == 5:
                five += 1

            elif bill == 10:
                if five == 0:
                    return False

                five -= 1       # Give $5 change
                ten += 1        # Keep the customer's $10 bill

            else:  # bill == 20
                # Prefer giving one $10 and one $5.
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1

                # Otherwise, give three $5 bills.
                elif five >= 3:
                    five -= 3

                else:
                    return False

        return True