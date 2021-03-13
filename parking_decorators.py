import sys


class ParkingApp:
    function_dict = {}

    def parking_functions(self, *args):
        def decorator(fn):
            self.function_dict[args[0]] = fn
            return fn

        return decorator

    def run(self):
        try:
            filename = 'input.txt'
            with open(filename) as file:
                for line in file:
                    line_split = line.split()
                    for funct in self.function_dict.keys():
                        if funct.split()[0] == line.split()[0]:
                            function_to_be_called = self.function_dict[funct]
                            args = (line_split[1:])
                            returned_value = function_to_be_called(*args)
                            if returned_value:
                                print(returned_value)
                            else:
                                print('None')
                            break

        except Exception as e:
            print(e)

if __name__ == '__main__':
    app = ParkingApp()
    app.run()