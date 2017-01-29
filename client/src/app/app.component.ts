import {Component, OnInit} from '@angular/core';
import {ServicesService} from "./service/services.service";


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{

  specification: {};
  result: Array<string>;
  loading: boolean;

  constructor(private service: ServicesService) {}

  ngOnInit(): void {
    this.loading = false;
    this.specification = {
      HaveQuickCharge: null,
      HaveTouchScreen: null,
      HaveAccelerometer: null,
      HaveProximitySensor: null,
      HaveLightSensor: null,
      Magnetometer: null,
      HaveGyroscope: null,
      HaveBarometer: null,
      HaveAltimeter: null,
      HaveGravitySensor: null,
      HaveIrisScanner: null,
      HaveFingerprintScanner: null,
      HaveThermometer: null,
      HaveHygrometer: null,
      HaveRAM: null,
      HaveMemory: null,
      HaveBattery: null,
      HaveWeight: null,
    }

  }

  search() {
    this.loading = true;
    this.result = [];
    this.service.search(this.specification)
        .subscribe(
          phones => {
            this.result = phones;
            this.loading = false;
          },
          error => console.error(error)
        );
  }



}
