import { Component, OnInit, Input } from '@angular/core';
import { Transaction } from '../transaction';

@Component({
  selector: 'app-transaction',
  templateUrl: './transaction.component.html',
  styleUrls: ['./transaction.component.css']
})
export class TransactionComponent implements OnInit {
  @Input() transaction?: Transaction

  constructor() { }

  ngOnInit(): void {
  }

  executeTransaction(): void {

  }

  canBeExecuted(): boolean {
    return this.transaction?.state == "EN_COURS" &&
      (this.transaction?.type == "DEPOT" || this.transaction?.type == "RETRAIT");
  }

}
