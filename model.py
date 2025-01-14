class Model:
    def __init__(self):
        self.value = '0'
        self.prev_value = ''
        self.operator = ''


    def calculate(self, caption):
        caption = str(caption)
        operators = ['+', '-', '*', '/']
        if caption == 'C':
            self.__clear()

        elif caption == '=':
            self.__evaluate_and_clear()

        elif caption in operators:
            self.__calculate_and_set_operator(caption)

        elif caption.isdigit():
            self.__append_digit(caption)

        elif caption == '+/-':
            self.__toggle_sign()

        elif caption == '%':
            self.__percent()

        elif caption == '.':
            self.__append_dot()

        else:
            pass

        return self.value


    def __clear(self):
        self.value = '0'
        self.prev_value = ''
        self.operator = ''


    def __evaluate_and_clear(self):
        if self.prev_value and self.operator:
            self.value = str(self.__evaluate())
            self.prev_value = ''
            self.operator = ''


    def __calculate_and_set_operator(self, operator):
        if self.prev_value and self.operator:
            self.value = str(self.__evaluate())
        self.operator = operator
        self.prev_value = self.value
        self.value = '0'


    def __append_digit(self, digit):
        zero = self.value == '0'
        negative_zero = self.value == '-0'
        if zero:
            self.value = ''
        elif negative_zero:
            self.value = '-'
        self.value += digit


    def __toggle_sign(self):
        if self.value.startswith('-'):
            self.value = self.value[1:]
        else:
            self.value = '-' + self.value

    def __percent(self):
        if self.value != '0':
            result = float(self.value) / 100
            if result.is_integer():
                result = int(result)
            self.value = str(result)

    def __append_dot(self):
        if '.' not in self.value:
            self.value += '.'

    def __evaluate(self):
        float_val = self.value.endswith('.0') or self.prev_value.endswith('.0')
        result = eval(self.prev_value + self.operator + self.value)
        if not float_val:
            result = int(result)
        return result

