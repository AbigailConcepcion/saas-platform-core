import { useEffect, useState } from "react";
import api from "../lib/api";

export default function Dashboard() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    api.get("products/").then(res => setProducts(res.data));
  }, []);

  return (
    <div className="p-10 grid grid-cols-3 gap-6">
      {products.map(p => (
        <div key={p.id} className="bg-white shadow rounded-2xl p-6">
          <h2 className="text-xl font-bold">{p.name}</h2>
          <p>{p.description}</p>
          <p className="mt-2 font-semibold">${p.price}</p>
        </div>
      ))}
    </div>
  );
}
