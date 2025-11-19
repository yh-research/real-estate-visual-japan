import React from "react";
import Chart from "../components/Chart"
import Map from "../components/Map";
import shibuyaData from "../../data/json/shibuya.json"


export default function SibuyaPage() {
    const { metrics, prefecture, city, ai_comment } = shibuyaData;
    const markers = [{ name: city, lat: 35.6618, lng: 139.7041}];

    return (
        <div style={({ padding: "20px"})}>
            <h1>{prefecture} {city} 不動産データ</h1>

            <Chart title="人口推移" labels={metrics.year} data={metrics.population} />
            <Chart title="地価推移" labels={metrics.year} data={metrics.land_price} color="rgba(255,99, 132, 1" />
            <Chart title="空き家率" labels={metrics.year} data={metrics.vacancy_rate} color="rgba(54,162,235,1)" />

            <Map center={[35.6618, 139.7041]} markers={markers} />

            <div style={{ marginTop: "20px", padding: "10px", backgroundColor: "#fofofo"}}>
                <h2>AIコメント</h2>
                <p>{ai_comment.summary}</p>
            </div>
        </div>
    );
}