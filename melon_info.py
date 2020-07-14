"""Print out all the melons in our inventory."""

from melons import melons


def print_all_melon_info(melons):
    """Print each melon with corresponding attribute information."""

    for melon_name, attributes in melons.items():
        print(f'{melon_name.upper()}:')
        for attribute, value in attributes.items():
            print(f'\t{attribute}: {value}')


print_all_melon_info(melons)
