from typing import Dict, List, Any
import ast
class OrderBook:
    """
    A class to maintain a collection of orders, each with a unique ID and a float value.
    Supports adding, removing, and summarizing orders.
    """
    def __init__(self) -> None:
        self.orders: Dict[str, float] = {}
    def add_order(self, order_id: str, value: float) -> None:
        """
        Adds an order with the given ID and value.
        """
        self.orders[order_id] = value
    def remove_order(self, order_id: str) -> None:
        """
        Removes the order with the given ID if it exists.
        """
        self.orders.pop(order_id, None)
    def summarize(self) -> str:
        """
        Returns a summary string with the count and average value of current orders.
        """
        count = len(self.orders)
        avg = sum(self.orders.values()) / count if count > 0 else 0.0
        return f"count={count}, avg={avg:.1f}"
def main() -> None:
    """
    Reads a list of operations from user input and processes them using OrderBook.
    """
    user_input = input()
    try:
        ops: List[Dict[str, Any]] = ast.literal_eval(user_input)
    except Exception:
        print("Invalid input format.")
        return
    ob = OrderBook()
    for op in ops:
        if op.get('op') == 'add':
            ob.add_order(op['id'], float(op['value']))
        elif op.get('op') == 'remove':
            ob.remove_order(op['id'])
    print(ob.summarize())
if __name__ == "__main__":
    main()