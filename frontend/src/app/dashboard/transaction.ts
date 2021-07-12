export interface Transaction {
  id: number;
  created: string;
  code: string;
  type: string;
  state: string;
  owner: number;
  montant: number;
  from_currency: string;
  to_currency: string;
}
