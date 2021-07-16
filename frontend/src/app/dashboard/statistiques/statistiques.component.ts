import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-statistiques',
  templateUrl: './statistiques.component.html',
  styleUrls: ['./statistiques.component.css']
})
export class StatistiquesComponent implements OnInit {
  selected : string = 'TRANSACTIONS';

  constructor() { }

  ngOnInit(): void {
  }

  onSelectedTransaction(type: string): void {
    this.selected = type;
  }
}
