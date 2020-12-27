#!/usr/bin/python

class FilterModule(object):
    def filters(self):
        return {
            'add_prop_from_list': self.add_prop_from_list,
        }

    def add_prop_from_list(self, input_list, name, prop_list):
        if len(prop_list) != len(input_list):
            raise "Lists must have same length."
        return [{name: prop_list[idx], **item} for idx, item in enumerate(input_list)]
