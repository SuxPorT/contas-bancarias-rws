import { NgModule, LOCALE_ID } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { Route, RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule, registerLocaleData } from '@angular/common';

import { AppComponent } from './app.component';
import { HeaderComponent } from './static/header/header.component';
import { AccountListComponent } from './components/account-list/account-list.component';
import { FooterComponent } from './static/footer/footer.component';
import { AngularMaterialModule } from './material/angular-material/angular-material.module';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import localePt from '@angular/common/locales/pt';

import { AccountDialogComponent } from './components/account-dialog/account-dialog.component';

const routes: Route[] = [
  { path: '', component: AppComponent },
];

registerLocaleData(localePt);


@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    AccountListComponent,
    FooterComponent,
    AccountDialogComponent
  ],
  imports: [
    BrowserModule,
    CommonModule,
    FormsModule,
    HttpClientModule,
    BrowserAnimationsModule,
    AngularMaterialModule,
    RouterModule.forRoot(routes)
  ],
  providers: [{
    provide: LOCALE_ID,
    useValue: 'pt-BR'
  }],
  bootstrap: [AppComponent]
})
export class AppModule { }
