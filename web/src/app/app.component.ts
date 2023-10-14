import { Component } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { AppService } from './app.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  selection: string | undefined;
  title = 'web';
  form = new FormGroup({
    textInput: new FormControl<string>(''),
    fileInput: new FormControl<File | null>(null),
  });
  commonWordsUsed: string[][] = [];

  constructor(
    private service: AppService,
  ) { }

  onFileChange(event: any) {
    const file = event.target.files[0];
    this.form.patchValue({
      fileInput: file,
    });
  }

  onSubmit() {
    const formData = new FormData();
    
    const data = this.form.get(
      this.selection === 'text-input' ? 'textInput' : 'fileInput'
    )?.value;
    
    if (!data) return;

    formData.append('text', data);

    this.service.getCommonWordsUsed(formData).subscribe(data => {
      this.commonWordsUsed = data;
    });
  }
}
