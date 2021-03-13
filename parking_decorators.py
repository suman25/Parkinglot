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
            filename = sys.argv[1]
            is_valid_command = 0
            with open(filename) as file:
                for line in file:
                    line_split = line.split()
                    for funct in self.function_dict.keys():
                        if funct.split()[0] == line.split()[0]:
                            is_valid_command = 1
                            function_to_be_called = self.function_dict[funct]
                            args = (line_split[1:])
                            returned_value = function_to_be_called(*args)
                            if returned_value:
                                if type(returned_value)== list:
                                    print(*returned_value ,sep=",")
                                else:
                                    print(returned_value)
                            else:
                                print('None')
                            break
                    if not is_valid_command:
                        print('Please type a valid command ')
        except IndexError as ex:
            if len(sys.argv) < 2:
                print('please give a filename as input')
                exit(1)
            else:
                print('Found some issue while executing the command')
        except Exception as e:
            print('Found some issue while executing the command')

if __name__ == '__main__':
    app = ParkingApp()
    app.run()