import flet as ft
import flet_datatable2 as fdt



def last_transactions():

    columns = [fdt.DataColumn2(label="#"),
               fdt.DataColumn2(label="Date"),
               fdt.DataColumn2(label="Produits"),
               fdt.DataColumn2(label="Montant"),
               fdt.DataColumn2(label="Moyen de Paiement"),
               fdt.DataColumn2(label="Référence")]
    
    rows = [
        fdt.DataRow2([ft.DataCell(ft.Text("1")), ft.DataCell(ft.Text("21/04/2025")), ft.DataCell(ft.Text("Lait Incolac Moyen")), ft.DataCell(ft.Text("5300")), ft.DataCell(ft.Text("CASH")), ft.DataCell(ft.Text("VE13465743")),]),
        fdt.DataRow2([ft.DataCell(ft.Text("1")), ft.DataCell(ft.Text("21/04/2025")), ft.DataCell(ft.Text("Lait Incolac Moyen")), ft.DataCell(ft.Text("5300")), ft.DataCell(ft.Text("CASH")), ft.DataCell(ft.Text("VE13465743")),]),
        fdt.DataRow2([ft.DataCell(ft.Text("1")), ft.DataCell(ft.Text("21/04/2025")), ft.DataCell(ft.Text("Lait Incolac Moyen")), ft.DataCell(ft.Text("5300")), ft.DataCell(ft.Text("CASH")), ft.DataCell(ft.Text("VE13465743")),]),
        fdt.DataRow2([ft.DataCell(ft.Text("1")), ft.DataCell(ft.Text("21/04/2025")), ft.DataCell(ft.Text("Lait Incolac Moyen")), ft.DataCell(ft.Text("5300")), ft.DataCell(ft.Text("CASH")), ft.DataCell(ft.Text("VE13465743")),]),
        fdt.DataRow2([ft.DataCell(ft.Text("1")), ft.DataCell(ft.Text("21/04/2025")), ft.DataCell(ft.Text("Lait Incolac Moyen")), ft.DataCell(ft.Text("5300")), ft.DataCell(ft.Text("CASH")), ft.DataCell(ft.Text("VE13465743")),])



    ]

    return ft.Container(
       ft.Column(
           [    ft.Text("Transactions récentes", font_family="PoppinsBold", color=ft.Colors.PRIMARY),
                ft.Divider(ft.Colors.PRIMARY),
                fdt.DataTable2(
                    columns=columns,
                    rows=rows,
                    empty=ft.Text("Aucune transaction enregistrée")
                ),
           ]
       ),
        expand=True,
        bgcolor=ft.Colors.SURFACE,
        padding=10,
        border_radius=10,
    )

