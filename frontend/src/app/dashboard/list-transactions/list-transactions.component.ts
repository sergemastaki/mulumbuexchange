import { Component, OnInit, Input } from '@angular/core';
import { Transaction } from '../transaction';
import { TransactionService } from '../transaction.service';

@Component({
  selector: 'app-list-transactions',
  templateUrl: './list-transactions.component.html',
  styleUrls: ['./list-transactions.component.css']
})
export class ListTransactionsComponent implements OnInit {
  @Input() type?: string
  transactions: Transaction[] = [];

  constructor(private transactionService: TransactionService) { }

  getTransactions(): void {
    this.transactionService.getTransactions()
          .subscribe(transactions => this.keepFilteredTransactions(transactions));
  }

  keepFilteredTransactions(transactions: Transaction[]): void {
    if(this.type === 'ATTENTE') {
      this.transactions = transactions.filter(transaction => {
        return transaction.type === 'DEPOT' || transaction.type === 'RETRAIT'
      });
    } else {
      this.transactions = transactions.filter(transaction => transaction.type === this.type);
    }
  }

  ngOnInit(): void {
    this.getTransactions()
  }

}
