import { Component, OnInit } from '@angular/core';
import { Transaction } from '../transaction';

@Component({
  selector: 'app-transaction',
  templateUrl: './transaction.component.html',
  styleUrls: ['./transaction.component.css']
})
export class TransactionComponent implements OnInit {
  transaction: Transaction = {
    id: 1,
    created: '2-2-2020',
    code: 'ty',
    type: 'DEPOT',
    state: 'EN_COURS',
    owner: 1,
    montant: 20,
    from_currency: 'BTC',
    to_currency: 'USDT'
  };

  constructor() { }

  ngOnInit(): void {
  }

}
