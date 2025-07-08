import React from "react";

const KarigarHomePage = () => {
  const services = [
    { label: "Laborer", image: "/icons/laborer.png" },
    { label: "Electrician", image: "/icons/electrician.png" },
    { label: "Plumber", image: "/icons/plumber.png" },
    { label: "Painter", image: "/icons/painter.png" },
    { label: "Marble Worker", image: "/icons/marble_worker.png" },
  ];

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow">
        <div className="container mx-auto px-4 py-4 flex items-center justify-between">
          <h1 className="text-2xl font-bold text-orange-600 flex items-center">
            <span className="text-3xl text-black font-extrabold mr-2">K</span>
            ARIGAR
          </h1>
          <input
            type="text"
            placeholder="Search Hominggar"
            className="border rounded-full px-4 py-2 text-gray-700 w-80 shadow-md"
          />
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto px-4 py-10">
        <div className="grid grid-cols-2 sm:grid-cols-3 gap-8">
          {services.map((service) => (
            <div
              key={service.label}
              className="flex flex-col items-center bg-white p-6 rounded-2xl shadow-md hover:shadow-lg transition-shadow"
            >
              <img
                src={service.image}
                alt={service.label}
                className="w-20 h-20 object-cover mb-4"
              />
              <h3 className="text-lg font-semibold text-gray-700">
                {service.label}
              </h3>
            </div>
          ))}
        </div>
      </main>
    </div>
  );
};

export default KarigarHomePage;