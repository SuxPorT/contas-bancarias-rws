import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Conta } from '../models/conta';

@Injectable({
  providedIn: 'root'
})


export class ContaService {
  url = 'http://127.0.0.1:5000/contas';

  constructor(private http: HttpClient) { }

  getAll(): Observable<Conta[]> {
    return this.http.get<Conta[]>(this.url);
  }

  getById(id: number): Observable<Conta> {
    return this.http.get<Conta>(`${this.url}/${id}`);
  }

  post(): Observable<Conta> {
    return this.http.post<Conta>(this.url, null);
  }

  update(conta: Conta): Observable<any> {
    return this.http.put<any>(`${this.url}/${conta.id}`, conta);
  }

  delete(id: number): Observable<any> {
    return this.http.delete<any>(`${this.url}/${id}`);
  }
}
