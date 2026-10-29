# Function signatures
def calculate_discount(price: float, percent: int) -> float:
    return price * (1 - percent / 100)


if __name__ == "__main__":
    discount = calculate_discount(100, 2)
    print(f"Discount: {discount}")

# 
# 
# cd ~/projects/beginers/python_type$ uv run python -c "import python_type.five_essentials;print('ok')"
# 