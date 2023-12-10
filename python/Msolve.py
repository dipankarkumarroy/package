def calculate(expression, **kwargs):
    try:
        result = eval(expression, kwargs)
        return result
    except NameError:
        print("Error: Make sure the variables in the expression match the provided keyword arguments.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


