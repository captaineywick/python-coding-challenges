from typing import List


class BestTimeBuyStockSolutionIII:
    @staticmethod
    def max_profit(prices: List[int]) -> int:
        # buy1: Best balance after buying first stock (negative because we spend money)
        # sell1: Best profit after selling first stock
        # buy2: Best balance after buying second stock (using profit from first)
        # sell2: Best profit after selling second stock (final answer)
        buy1 = buy2 = float("-inf")
        sell1 = sell2 = 0

        for index, price in enumerate(prices, 1):
            print(f"Iterate #{index}")

            # ===== 1st Transaction =====
            # Decide whether to keep old buy1 OR buy at current price
            # (-price means spending money)
            print(f"buy1: {buy1}, -price: {-price}")
            buy1 = max(buy1, -price)
            print(f"buy1 max: {buy1}")

            # Decide whether to keep old sell1 OR sell now after buying at buy1
            print(f"sell1: {sell1}, buy1 + price: {buy1 + price}")
            sell1 = max(sell1, buy1 + price)
            print(f"sell1 max: {sell1}")

            # ===== 2nd Transaction =====
            # Decide whether to keep old buy2 OR buy now using profit from sell1
            print(f"buy2: {buy2}, sell1 - price: {sell1 - price}")
            buy2 = max(buy2, sell1 - price)
            print(f"buy2 max: {buy2}")

            # Decide whether to keep old sell2 OR sell now after second buy
            print(f"sell2: {sell2}, buy2 + price: {buy2 + price}")
            sell2 = max(sell2, buy2 + price)
            print(f"sell2 max: {sell2}")
            print()

        # sell2 will contain the maximum profit from at most 2 transactions
        return sell2
