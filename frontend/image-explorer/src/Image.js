import React from 'react';

export default function Image(props) {
    console.log(props.imageInfo.image);
    return (
        <div>
            <img src={props.imageInfo.image} alt="thumbnail"/>
        </div>
    );
}
