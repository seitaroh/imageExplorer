import React from 'react';
import { useState } from 'react';
import { useEffect } from 'react';
import Image from './Image';

// 動物園の写真のみ取得、動物の写真のみ取得のようなフィルタリング
export default function Card(props) {
    const imagesRequestUrl = 'http://127.0.0.1:8000/api/images/';
    const [imagesInfo, setImagesInfo] = useState([]);
    useEffect(() => {
        fetch(imagesRequestUrl)
        .then(response => response.json())
        .then(imagesInfo => setImagesInfo(imagesInfo))
    }, []);
    console.log(imagesInfo);
    const imageList = imagesInfo.map((imageInfo) => <Image imageInfo={imageInfo} key={imageInfo.id}/>);
    // 現状は画像リストを表示している
    // 実際にはimageとCardを結び付けたい.Cardのthumbnailとimageのidを結び付ける？
    // またはCardの属性として画像を持たせる
    return (
        <div>
            {imageList}
        </div>
    );
}
