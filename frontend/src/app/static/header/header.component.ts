import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  externalUrl = 'https://www.pucpr.br/';
  title: string = 'Contas Bancárias';

  constructor(private router: Router) { }

  ngOnInit(): void {
  }

  navigate(): void {
    window.open(this.externalUrl, "_blank");
  }

}
