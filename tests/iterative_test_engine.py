from typing import Dict, List
import copy
import abc


class IterativeTestor:
    def __init__(self, loop_nest: Dict[str, List], key_list: List):
        self.__loop_nest = loop_nest
        self.__key_list = key_list

    def get_args_combinations(self):
        self.__com_list = []
        self.__recursive_looping()
        return self.__com_list

    def __recursive_looping(self, args=[], depth=0):
        _args = copy.copy(args)
        if depth >= len(self.__key_list):
            self.__com_list.append(tuple(_args))
        else:
            for element in self.__loop_nest[self.__key_list[depth]]:
                self.__recursive_looping(
                    args=_args + [element], depth=depth + 1)

    def test_get_args_combinations(self):
        com_list = self.get_args_combinations()
        assert len(com_list) == len(set(com_list))
        print('Confirm no replicate combination')
        for com in com_list:
            for i, element in enumerate(com):
                assert element in self.__loop_nest[self.__key_list[i]]
        print('Confirm elements in combination is correct')
        return True

    def test_template(self, *args):
        """
        Put the test script here

        Example:

        assert func(*args) is not None
        """
        pass

    def loop_test_template(self):
        assert self.test_get_args_combinations()
        for com in self.get_args_combinations():
            self.test_template(*com)
        return True
