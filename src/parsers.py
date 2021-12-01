import argparse


class NumSeatsAction(argparse.Action):
    ''' Class of a new action for arguments that must be initialized with integers > 3
    '''
    def __call__(self, parser, namespace, values, option_string=None):
        if values <= 3:
            parser.error('Minimum integer value for {} is 4.'.format(option_string))
        setattr(namespace, self.dest, values)


class MaxWeightAction(argparse.Action):
    ''' Class of a new action for arguments that must be initialized with integers > 1 and < 20
    '''
    def __call__(self, parser, namespace, values, option_string=None):
        if values < 1 or values > 20:
            parser.error('Integer values for {} must be from interval [1, 20].'.format(option_string))
        setattr(namespace, self.dest, values)


class NatNumbAction(argparse.Action):
    ''' Class of a new action for arguments that must be initialized with integers >= 1
    '''
    def __call__(self, parser, namespace, values, option_string=None):
        if values < 1:
            parser.error('Integer values for {} must be > 1.'.format(option_string))
        setattr(namespace, self.dest, values)


class PositiveNumberAction(argparse.Action):
    ''' Class of a new action for arguments that must be initialized with floats > 0
    '''
    def __call__(self, parser, namespace, values, option_string=None):
        if values <= 0:
            parser.error('Values for {} must be > 0.'.format(option_string))
        setattr(namespace, self.dest, values)


def main_parser():
    '''
    Creates help file and parses command line arguments for the main script, i.e. run.py
    Parameters:
        - no input parameters
    Returns:
        - args, class 'argparse.Namespace'
    '''

    formatter = lambda prog: argparse.RawTextHelpFormatter(prog, max_help_position=50)
    parser = argparse.ArgumentParser(
            description='Solves Knapsack problem for committee selection',
            add_help=False,
            formatter_class=formatter,
            )

    # required arguments
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument(
            '--n_nodes',
            action=NumSeatsAction,
            type=int,
            required=True,
            metavar='{4,5,...}',
            help='number of nodes in the network',
            )
    required_args.add_argument(
            '--n_seats',
            action=NumSeatsAction,
            type=int,
            required=True,
            metavar='{4,5,...}',
            help='number of seats in the committee',
            )
    required_args.add_argument(
            '--zipfc',
            action=PositiveNumberAction,
            type=float,
            required=True,
            metavar='> 0',
            help='zipf coefficient',
            )
    required_args.add_argument(
            '--mode',
            type=str,
            choices=['stop', 'overtake'],
            required=True,
            help='mode to simulate: either stop or overtake the committee',
            )

    # optimal arguments
    optional_args = parser.add_argument_group('optional arguments')
    optional_args.add_argument(
            '-h',
            '--help',
            action='help',
            help='show this help message and exit',
            )
    optional_args.add_argument(
            '--seed',
            type=int,
            action=NatNumbAction,
            required=False,
            default=2021,
            metavar='{1,2,...}',
            help='seed for random generator, defaults to 2021',
            )
    optional_args.add_argument(
            '--max_weight',
            type=int,
            action=MaxWeightAction,
            required=False,
            default=20,
            metavar='{1,2,...,20}',
            help='maximum value of voting power, defaults to 20',
            )
    optional_args.add_argument(
            '--solver',
            type=str,
            required=False,
            default='glpk',
            help='solver name, defaults to glpk',
            )
    optional_args.add_argument(
            '--latex',
            action='store_true',
            default=False,
            help='use LaTeX in plots, defaults to False'
            )
    optional_args.add_argument(
            '--hide_plots',
            action='store_true',
            default=False,
            help='do not show plots, defaults to False'
            )
    optional_args.add_argument(
            '--novis',
            action='store_true',
            default=False,
            help='do visualize the results, defaults to False'
            )
    optional_args.add_argument(
            '--verbose',
            action='store_true',
            default=False,
            help='verbose outputs, defaults to False'
            )

    return parser


def attacker_cost_parser():
    '''
    Creates help file and parses command line arguments for the main script, i.e. run.py
    Parameters:
        - no input parameters
    Returns:
        - args, class 'argparse.Namespace'
    '''

    formatter = lambda prog: argparse.RawTextHelpFormatter(prog, max_help_position=50)
    parser = argparse.ArgumentParser(
            description='Computes attacker cost for different values of zipf coefficients',
            add_help=False,
            formatter_class=formatter,
            )

    # required arguments
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument(
            '--n_nodes',
            action=NumSeatsAction,
            type=int,
            required=True,
            metavar='{4,5,...}',
            help='number of nodes in the network',
            )
    required_args.add_argument(
            '--n_seats',
            action=NumSeatsAction,
            type=int,
            required=True,
            metavar='{4,5,...}',
            help='number of seats in the committee',
            )
    required_args.add_argument(
            '--mode',
            type=str,
            choices=['stop', 'overtake'],
            required=True,
            help='mode to simulate: either stop or overtake the committee',
            )

    # optimal arguments
    optional_args = parser.add_argument_group('optional arguments')
    optional_args.add_argument(
            '-h',
            '--help',
            action='help',
            help='show this help message and exit',
            )
    optional_args.add_argument(
            '--zipfc_min',
            action=PositiveNumberAction,
            type=float,
            required=False,
            metavar='> 0',
            default=0.5,
            help='minimum value of zipf coefficient, default to 0.5',
            )
    optional_args.add_argument(
            '--zipfc_max',
            action=PositiveNumberAction,
            type=float,
            required=False,
            metavar='> 0',
            default=1.5,
            help='maximum value of zipf coefficient, default to 1.5',
            )
    optional_args.add_argument(
            '--zipfc_step',
            action=PositiveNumberAction,
            type=float,
            required=False,
            metavar='> 0',
            default=0.01,
            help='step to generate range of zipf coefficients, default to 0.01',
            )
    optional_args.add_argument(
            '--solver',
            type=str,
            required=False,
            default='glpk',
            help='solver name, defaults to glpk',
            )
    optional_args.add_argument(
            '--latex',
            action='store_true',
            default=False,
            help='use LaTeX in plots, defaults to False'
            )
    optional_args.add_argument(
            '--hide_plots',
            action='store_true',
            default=False,
            help='do not show plots, defaults to False'
            )
    optional_args.add_argument(
            '--novis',
            action='store_true',
            default=False,
            help='do visualize the results, defaults to False'
            )
    optional_args.add_argument(
            '--verbose',
            action='store_true',
            default=False,
            help='verbose outputs, defaults to False'
            )
    optional_args.add_argument(
            '--csv',
            action='store_true',
            default=False,
            help='save data to CSV file, defaults to False'
            )

    return parser


def costs_parser():
    '''
    Creates help file and parses command line arguments for the main script, i.e. run.py
    Parameters:
        - no input parameters
    Returns:
        - args, class 'argparse.Namespace'
    '''

    formatter = lambda prog: argparse.RawTextHelpFormatter(prog, max_help_position=50)
    parser = argparse.ArgumentParser(
            description='Computes nodes costs for different values of zipf coefficients',
            add_help=False,
            formatter_class=formatter,
            )

    # required arguments
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument(
            '--n_nodes',
            action=NumSeatsAction,
            type=int,
            required=True,
            metavar='{4,5,...}',
            help='number of nodes in the network',
            )
    '''
    required_args.add_argument(
            '--n_seats',
            action=NumSeatsAction,
            type=int,
            required=True,
            metavar='{4,5,...}',
            help='number of seats in the committee',
            )
    '''

    # optimal arguments
    optional_args = parser.add_argument_group('optional arguments')
    optional_args.add_argument(
            '-h',
            '--help',
            action='help',
            help='show this help message and exit',
            )
    optional_args.add_argument(
            '--zipfc_min',
            action=PositiveNumberAction,
            type=float,
            required=False,
            metavar='> 0',
            default=0.5,
            help='minimum value of zipf coefficient, default to 0.5',
            )
    optional_args.add_argument(
            '--zipfc_max',
            action=PositiveNumberAction,
            type=float,
            required=False,
            metavar='> 0',
            default=1.5,
            help='maximum value of zipf coefficient, default to 1.5',
            )
    optional_args.add_argument(
            '--zipfc_step',
            action=PositiveNumberAction,
            type=float,
            required=False,
            metavar='> 0',
            default=0.1,
            help='step to generate range of zipf coefficients, default to 0.1',
            )
    optional_args.add_argument(
            '--latex',
            action='store_true',
            default=False,
            help='use LaTeX in plots, defaults to False'
            )
    optional_args.add_argument(
            '--hide_plots',
            action='store_true',
            default=False,
            help='do not show plots, defaults to False'
            )
    optional_args.add_argument(
            '--novis',
            action='store_true',
            default=False,
            help='do visualize the results, defaults to False'
            )
    optional_args.add_argument(
            '--verbose',
            action='store_true',
            default=False,
            help='verbose outputs, defaults to False'
            )
    optional_args.add_argument(
            '--csv',
            action='store_true',
            default=False,
            help='save data to CSV file, defaults to False'
            )

    return parser
