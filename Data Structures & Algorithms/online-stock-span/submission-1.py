class StockSpanner:

    def __init__(self):
        # Each item is: [price, span]
        self.stack = []

    def next(self, price: int) -> int:
        # Today's price always counts.
        span = 1

        # Combine all previous consecutive prices
        # that are less than or equal to today's price.
        while self.stack and self.stack[-1][0] <= price:
            previous_price, previous_span = self.stack.pop()
            span += previous_span

        # Save today's price and its complete span.
        self.stack.append([price, span])

        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)