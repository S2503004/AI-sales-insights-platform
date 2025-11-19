import React, {useEffect, useState} from 'react';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

export default function App(){
  const [data, setData] = useState([]);
  useEffect(()=>{
    // for demo, fetch static CSV from docs (replace with API in production)
    fetch('/data/sales_demo.csv').then(r=>r.text()).then(txt=>{
      const rows = txt.split('\n').slice(1).filter(Boolean).map(line=>{
        const [date,units_sold,price,marketing_spend] = line.split(',');
        return {date, units_sold: Number(units_sold), price: Number(price), marketing_spend: Number(marketing_spend), revenue: Number(units_sold)*Number(price)};
      });
      setData(rows);
    })
  },[]);
  return (
    <div style={{padding:20,fontFamily:'Arial'}}>
      <h1>Sales Insights Dashboard (Demo)</h1>
      <div style={{height:300}}>
        <ResponsiveContainer>
          <LineChart data={data}>
            <XAxis dataKey="date"/>
            <YAxis />
            <Tooltip />
            <Line type="monotone" dataKey="revenue" stroke="#8884d8" />
          </LineChart>
        </ResponsiveContainer>
      </div>
      <p>Demo dashboard using Recharts. Connect to /predict API for on-demand forecasting.</p>
    </div>
  );
}
