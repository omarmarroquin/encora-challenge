import { TestBed } from '@angular/core/testing';
import { AppComponent } from './app.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AppService } from './app.service';
import { of } from 'rxjs';

describe('AppComponent', () => {
  beforeEach(() => TestBed.configureTestingModule({
    declarations: [AppComponent],
    imports: [FormsModule, ReactiveFormsModule, HttpClientModule],
  }));

  it('should create the app', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    expect(app).toBeTruthy();
  });

  it('should update the file input control when a file is selected', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    const file = new File(['sample content'], 'sample.txt');
    const event = {
      target: {
        files: [file],
      },
    };
    app.onFileChange(event);
    expect(app.form.get('fileInput')?.value).toBe(file);
  });

  it('should not update the file input control when no file is selected', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
  
    const event = {
      target: {
        files: [],
      },
    };
    app.onFileChange(event);
  
    // Expect that fileInput remains null
    expect(app.form.get('fileInput')?.value).toBeUndefined();
  });

  it('should submit file data when a file is selected', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
  
    const file = new File(['sample content'], 'sample.txt');
    const event = {
      target: {
        files: [file],
      },
    };
    app.selection = 'file-input';
  
    // Ensure form data is updated with the selected file
    app.onFileChange(event);
  
    // Mock the service response
    const mockData = [['word1', 'word2']];
    const service = TestBed.inject(AppService);
    spyOn(service, 'getCommonWordsUsed').and.returnValue(of(mockData));
  
    app.onSubmit();
  
    // Expect commonWordsUsed to be updated with the service response
    expect(app.commonWordsUsed).toEqual(mockData);
  });
});
