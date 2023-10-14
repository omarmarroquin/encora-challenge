import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AppService {

  constructor(
    private http: HttpClient,
  ) { }

  getCommonWordsUsed(data: FormData) {
    return this.http.post<string[][]>('http://localhost:8000/common-words-used', data);
  }
}
