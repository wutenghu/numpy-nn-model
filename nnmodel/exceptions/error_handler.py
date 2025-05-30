

class ErrorHandler(Exception):
    class InvalidOptimizerType(Exception):
        def __init__(self, optimizer_type):
            self.optimizer_type = optimizer_type
            super().__init__(self.optimizer_type)

        def __str__(self):
            return f'Optimizer must be a string or Class of existing Optimizers'

    class InvalidOptimizerName(Exception):
        def __init__(self, optimizer_name):
            self.optimizer_name = optimizer_name
            super().__init__(self.optimizer_name)

        def __str__(self):
            return f'Optimizer with name {self.optimizer_name} does not exist'

    class InvalidLossType(Exception):
        def __init__(self, loss_type):
            self.loss_type = loss_type
            super().__init__(self.loss_type)

        def __str__(self):
            return f'Loss function must be a string or Class of existing Loss Functions'

    class InvalidLossName(Exception):
        def __init__(self, loss_name):
            self.loss_name = loss_name
            super().__init__(self.loss_name)

        def __str__(self):
            return f'Loss function with name {self.loss_name} does not exist'
        

    
    class InvalidActivationType(Exception):

            def __init__(self, activation_type):
                self.activation_type = activation_type
                super().__init__(self.activation_type)

            def __str__(self):
                return f'Activation must be a string, None or Class of existing Activation'

    class InvalidActivationName(Exception):

            def __init__(self, activation_name):
                self.activation_name = activation_name
                super().__init__(self.activation_name)

            def __str__(self):
                return f'Activation with name {self.activation_name} does not exist'

    class InvalidRecurrentLayer(Exception):

            def __init__(self, layer, access_recurrent):
                self.layer = layer
                self.access_recurrent = access_recurrent
                super().__init__(self.layer, self.access_recurrent)

            def __str__(self):
                if self.access_recurrent:
                    return f'{self.layer} is not a recurrent layer'
                else:
                    return f'{self.layer} is invalid. You can use all layers except recurrent'

    class InvalidSize2Variable(Exception):

            def __init__(self, variable_type, variable_name, min_acceptable_value):
                self.variable_type = variable_type
                self.variable_name = variable_name
                self.min_acceptable_value = min_acceptable_value
                super().__init__(self.variable_type, self.variable_name, self.min_acceptable_value)

            def __str__(self):
                add_message = ""
                if self.variable_name == "padding":
                    add_message = ', or string: "same"/"real same"/"valid"'

                return f' Unable to extract {self.variable_name} values from type {self.variable_type}; {self.variable_name} must be greater than or equal "{self.min_acceptable_value}" integer value, or list/tuple type of size 2 and contain greater than or equal "{self.min_acceptable_value}" integer values {add_message}'
    
    class InvalidIntegerValue(Exception):
            def __init__(self, variable_type, variable_name):
                self.variable_name = variable_name
                self.variable_type = variable_type
                super().__init__(self.variable_type, self.variable_name)

            def __str__(self):
                return f'Type of the variable {self.variable_name} must be positive integer, got {self.variable_type}'

    class InvalidFloatValue(Exception):
            def __init__(self, variable_type, variable_name):
                self.variable_name = variable_name
                self.variable_type = variable_type
                super().__init__(self.variable_type, self.variable_name)

            def __str__(self):
                return f'Type of the variable {self.variable_name} must be float and greater than or equal "0" , got {self.variable_type}'

    class InvalidInputDim(Exception):
            def __init__(self, variable_type, input_dim):
                self.input_dim = input_dim
                self.variable_type = variable_type
                super().__init__(self.variable_type, self.input_dim)

            def __str__(self):
                return f'''Unable to extract "input_shape" values from type {self.variable_type};\nPossibe cases:\n "input_shape" must be positive integer value or list/tuple type of size {self.input_dim} that contain positive integer values\nExample:\n for "Dense" layer "input_shape" only can be of two types: "123" or "(1, 123)"\n for "Conv2D" and some others layer "input_shape" must be only list/tuple type of size 3: (Channels, Height, Width), and contain integer value\n'''
    
    class InvalidShape(Exception):
            def __init__(self, variable_type):
                self.variable_type = variable_type
                super().__init__(self.variable_type)

            def __str__(self):
                return f'''Unable to extract "shape" values from type {self.variable_type};\nPossibe cases:\n "input_shape" must be positive integer value or list/tuple type that contain positive integer values'''

    class InvalidBoleanType(Exception):
            def __init__(self, variable_type, variable_name):
                self.variable_name = variable_name
                self.variable_type = variable_type
                super().__init__(self.variable_type, self.variable_name)

            def __str__(self):
                return f'Type of the variable {self.variable_name} must be boolean (True, False), got {self.variable_type}'