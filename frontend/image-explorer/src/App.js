import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <ImageSlider />
          <ImageUploader />
        </header>
      </div>
  );
}

class ImageSlider extends React.Component{
  render() {
    const title = "today's TNK";

    return (
        <div>
          <div>{title}</div>
        </div>
    );
  }
}

class ImageUploader extends React.Component{
  dragover_handler = (e) => {
    e.preventDefault();
  }

  dragenter_handler = (e) => {
    e.preventDefault();
  }

  dragleave_handler = (e) => {
    e.preventDefault();
  }

  drop_handler = (e) => {
    e.preventDefault();

    let data = e.dataTransfer,
        files = data.files;

    this.handleFiles(files)
  }

  click_handler = () => {
    let input_hidden = document.getElementById("input-hidden");
    input_hidden.click();
  }

  change_handler = () => {
    let input_hidden = document.getElementById("input-hidden")
    let files = input_hidden.files;
    this.handleFiles(files);
  }

  handleFiles = (files) => {
    for (let i = 0, len = files.length; i < len; i++) {
      if (this.validateImage(files[i]))
        this.previewAndUploadImage(files[i]);
    }
  }

  validateImage = (image) => {
    // check the type
    const validTypes = ['image/jpeg', 'image/png', 'image/gif'];
    if (validTypes.indexOf( image.type ) === -1) {
      alert("Invalid File Type");
      return false;
    }
    // check the size
    const maxSizeInBytes = 10e6; // 10MB
    if (image.size > maxSizeInBytes) {
      alert("File too large");
      return false;
    }
    return true;
  }

  previewAndUploadImage = (image) => {
    const imagePreviewRegion = document.getElementById("image-preview");
    // container
    let imgView = document.createElement("div");
    imgView.className = "image-view";
    imagePreviewRegion.appendChild(imgView);

    // previewing image
    let img = document.createElement("img");
    imgView.appendChild(img);

    // progress overlay
    let overlay = document.createElement("div");
    overlay.className = "overlay";
    imgView.appendChild(overlay);

    // read the image...
    let reader = new FileReader();
    reader.onload = (e) => {
      img.src = e.target.result;
    }
    reader.readAsDataURL(image);
  }

  render() {
    return (
        <div id="target"
             onDragEnter={this.dragenter_handler}
             onDragLeave={this.dragleave_handler}
             onDragOver={this.dragover_handler}
             onDrop={this.drop_handler}
             onClick={this.click_handler}>
          <div className="drop-message">
            Drag & Drop images or click to upload
          </div>
          <input id="input-hidden" style={{display: "none"}} type="file" accept="image/*" multiple
                 onChange={this.change_handler}/>
          <div id="image-preview"> </div>
        </div>

    )
  }
}


export default App;
