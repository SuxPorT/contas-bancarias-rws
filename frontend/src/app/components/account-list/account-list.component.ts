import { Component, OnInit } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import { Conta } from 'src/app/models/conta';
import { ContaService } from 'src/app/services/conta.service';
import { MatDialog } from '@angular/material/dialog';
import { AccountDialogComponent } from '../account-dialog/account-dialog.component';
import { FormControl, FormGroup } from '@angular/forms';


@Component({
  selector: 'app-account-list',
  styleUrls: ['account-list.component.css'],
  templateUrl: 'account-list.component.html',
})
export class AccountListComponent implements OnInit {

  displayedColumns = ['id', 'saldo', 'acoes'];
  contaDataSource = new MatTableDataSource<Conta>();

  constructor(private contaService: ContaService, public dialog: MatDialog) { }

  ngOnInit(): void {
    this.getListaContas();
  }

  openDialog(conta: Conta): void {
    const dialogRef = this.dialog.open(AccountDialogComponent, {
      width: '250px',
      data: { id: conta.id, valor: 0.0, operacao: false },
    });

    dialogRef.afterClosed().subscribe((result) => {
      if (result) {
        this.update(result);
      }
    });
  }

  getListaContas(): void {
    this.contaService.getAll().subscribe((result) => {
      this.contaDataSource = new MatTableDataSource<Conta>(result);

      console.log(this.contaDataSource.data);
    });
  }

  get(conta: Conta): void {
    this.contaService.getById(conta.id).subscribe((result) => {
      console.log(result);
    });
  }

  create(): void {
    this.contaService.post().subscribe((_result) => {
      this.getListaContas();
    });
  }

  update(data: any): void {
    this.contaService.update(data).subscribe((_result) => {});
    this.getListaContas();
  }

  delete(conta: Conta): void {
    this.contaService.delete(conta.id).subscribe((_result) => {
      this.getListaContas();
    });
  }
}
