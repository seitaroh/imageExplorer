import React, { useEffect, useState  } from "react";
import Card from "./Card";

export default function Page() {
    const cardsRequestUrl = 'http://127.0.0.1:8000/api/cards/';
    const [cardsInfo, setCardsInfo] = useState([]);
    useEffect(() => {
        fetch(cardsRequestUrl)
        .then(response => response.json())
        .then(cardsInfo => setCardsInfo(cardsInfo))
    }, []);
    const cardList = cardsInfo.map((cardInfo) => <Card info={cardInfo}/>);
    return (
    <div>
        {cardList}
    </div>
    );
}