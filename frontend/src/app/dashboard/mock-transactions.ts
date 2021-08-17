import { Transaction } from './transaction';

export const TRANSACTIONS: Transaction[] = [
  {
    id: 1,
    created: '2-2-2020',
    code: 'ty',
    type: 'DEPOT',
    state: 'EN_COURS',
    owner: 1,
    montant: 20,
    from_currency: 'BTC',
    to_currency: 'USDT'
  },
  {
    id: 2,
    created: '10-2-2020',
    code: 'ty',
    type: 'DEPOT',
    state: 'EN_COURS',
    owner: 1,
    montant: 20,
    from_currency: 'BTC',
    to_currency: 'USDT'
  },
  {
    id: 3,
    created: '8-2-2020',
    code: 'ty',
    type: 'ACHAT',
    state: 'EN_COURS',
    owner: 1,
    montant: 20,
    from_currency: 'BTC',
    to_currency: 'USDT'
  },
  {
    id: 4,
    created: '2-2-2021',
    code: 'ty',
    type: 'VENTE',
    state: 'EN_COURS',
    owner: 1,
    montant: 20,
    from_currency: 'BTC',
    to_currency: 'USDT'
  },
  {
    id: 5,
    created: '2-4-2020',
    code: 'ty',
    type: 'DEPOT',
    state: 'EXECUTER',
    owner: 1,
    montant: 20,
    from_currency: 'BTC',
    to_currency: 'USDT'
  },
  {
    id: 6,
    created: '2-2-2019',
    code: 'ty',
    type: 'RETRAIT',
    state: 'EXECUTER',
    owner: 1,
    montant: 20,
    from_currency: 'BTC',
    to_currency: 'USDT'
  },
  {
    id: 7 ,
    created: '1-2-2020',
    code: 'ty',
    type: 'DEPOT',
    state: 'ANNULER',
    owner: 1,
    montant: 20,
    from_currency: 'BTC',
    to_currency: 'USDT'
  }
];
