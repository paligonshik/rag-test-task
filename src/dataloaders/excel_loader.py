"""Excel data loader for invoice data."""

from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass
class DataContext:
    """Container for all loaded dataframes and pre-computed views."""

    clients: pd.DataFrame
    invoices: pd.DataFrame
    line_items: pd.DataFrame
    # Pre-merged master dataframe for complex queries
    merged: pd.DataFrame

    def get_dataframes_dict(self) -> dict[str, pd.DataFrame]:
        """Return a dict of dataframes for code execution context."""
        return {
            "clients": self.clients,
            "invoices": self.invoices,
            "line_items": self.line_items,
            "merged": self.merged,
        }


def load_data(data_dir: str | Path) -> DataContext:
    """Load all Excel files and create DataContext.

    Args:
        data_dir: Path to the directory containing Excel files.

    Returns:
        DataContext with all loaded and processed dataframes.
    """
    data_path = Path(data_dir)

    # Load individual tables
    clients = pd.read_excel(data_path / "Clients.xlsx")
    invoices = pd.read_excel(data_path / "Invoices.xlsx")
    line_items = pd.read_excel(data_path / "InvoiceLineItems.xlsx")

    # Ensure date columns are proper datetime types
    invoices["invoice_date"] = pd.to_datetime(invoices["invoice_date"])
    invoices["due_date"] = pd.to_datetime(invoices["due_date"])

    # Create pre-merged master dataframe for complex queries
    merged = (
        clients.merge(invoices, on="client_id", how="left")
        .merge(line_items, on="invoice_id", how="left")
    )

    # Pre-compute line_total column (quantity * unit_price * (1 + tax_rate))
    merged["line_total"] = (
        merged["quantity"] * merged["unit_price"] * (1 + merged["tax_rate"])
    )

    return DataContext(
        clients=clients,
        invoices=invoices,
        line_items=line_items,
        merged=merged,
    )

