# 🚚 Object-Oriented Logistics Management System

An advanced Python-based logistics and delivery management system built using Object-Oriented Programming (OOP) principles. This project is developed as part of academic coursework to model real-world supply chain entities, package tracking, courier capacity management, and hub networks.

---

## 🏗️ Project Architecture & Classes

The system is modularized into core OOP classes representing different domains of a logistics network:

*   **Package**: Manages shipment details, tracking numbers, destinations, weights, priorities, and delivery statuses (Registered, In Transit, Delivered).
*   **Hub**: Represents distribution centers with specific geographical coordinates, local inventories, and connected network routes.
*   **Courier**: Tracks courier profiles, weight capacities, active delivery loads, and real-time availability.
*   **Route**: Models paths and distances (in kilometers) between different hubs.
*   **DeliverySystem**: The central controller managing the registry of packages, hubs, couriers, routes, and sorting/filtering logic.
