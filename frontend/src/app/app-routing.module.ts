import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { StatistiquesComponent } from './dashboard/statistiques/statistiques.component';
import { TransactionComponent } from './dashboard/transaction/transaction.component';
import { TransactionsComponent } from './dashboard/transactions/transactions.component';
import { LoginComponent } from './auth/login/login.component';

const routes: Routes = [
  {
    path: 'dashboard',
    component: DashboardComponent,
    children: [
      { path: 'statistiques', component: StatistiquesComponent },
      { path: 'transactions', component: TransactionsComponent },
      { path: 'transaction-details', component: TransactionComponent },
    ]
  },
  { path: 'login', component: LoginComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
