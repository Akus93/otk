import { Injectable } from '@angular/core';
import { Http, Headers, Response } from '@angular/http';
import { Observable } from 'rxjs';

@Injectable()
export class ServicesService {

  address = 'http://127.0.0.1:5000/api/';

  constructor(private http: Http) { }

  public search(params: {}): Observable<any> {

    let url = this.address + 'search/';
    let body = JSON.stringify(params);
    let options = {
      headers: new Headers({
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      })
    };

    return this.http.post(url, body, options)
      .map((res: Response) => res.json())
      .catch(this.handleError);
  }

  private handleError (error: Response) {
    return Observable.throw(error.json());
  }
}
