
import csv
import sys
import json
from typing import List
from options import OutputOption
from rich import print
from rich.console import Console
from rich.table import Table



def print_beauty(list_of_dict: List[dict], output: OutputOption):
    
    if output == OutputOption.csv:
        fieldnames = list_of_dict[0].keys()
        writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(list_of_dict)

    elif output == OutputOption.json:
        print(json.dumps(list_of_dict, indent=4))

    elif output == OutputOption.table:

        table = Table()
        headers = list_of_dict[0].keys()
        for h in headers:
            table.add_column(str(h), style="magenta")
        for repo in list_of_dict:
            table.add_row(*[str(r) for r in repo.values()])



        console = Console()
        console.print(table)