import sys


class ParkingApp:
    function_dict = {}

    def parking_functions(self, *args):
        def decorator(fn):
            """
            A decorator which would create a dict containing the command as key and value as function
            which will make it easier to add any commands in the future
            :param fn: funtion
            :return:
            """
            self.function_dict[args[0]] = fn
            return fn

        return decorator

    def run(self):
        """
        Get the filename as input from commandline and call the functions based on commands in input file
        :return:
        """
        try:
            filename = sys.argv[1]
            with open(filename) as file:
                for line in file:
                    line_split = line.split()
                    for func in self.function_dict.keys():
                        is_valid_command = 0
                        if func.split()[0] == line.split()[0]:
                            is_valid_command = 1
                            function_to_be_called = self.function_dict[func]
                            args = (line_split[1:])
                            returned_value = function_to_be_called(*args)
                            if returned_value:
                                if type(returned_value) == list:
                                    print(*returned_value, sep=",")
                                else:
                                    print(returned_value)
                            else:
                                print('None')
                            break
                    if not is_valid_command:
                        print('Please type a valid command ')
        except IndexError:
            if len(sys.argv) < 2:
                print('please give a filename as input')
                exit(1)
            else:
                print('Found some issue while executing the command')
        except Exception:
            print('Found some issue while executing the command')


if __name__ == '__main__':
    app = ParkingApp()
    app.run()
