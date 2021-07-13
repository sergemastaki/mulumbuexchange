import { Component, OnInit } from '@angular/core';
import {FormControl, Validators} from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  email = new FormControl('', [Validators.required, Validators.email]);
  password = new FormControl('', [Validators.required]);
  hide = true;

  constructor() { }

  ngOnInit(): void {
  }

  getEmailErrorMessage() {
    if (this.email.hasError('required')) {
      return 'Email obligatoire';
    }

    return this.email.hasError('email') ? 'Email non valide' : '';
  }

  getPasswordErrorMessage() {
    return this.password.hasError('required') ? 'Mot de passe obligatoire' : '';
  }

}
