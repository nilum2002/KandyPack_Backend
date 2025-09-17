-- Insert dummy data into Users table (unchanged)
INSERT INTO users (user_id, user_name, password_hash, role, created_at) VALUES
('a1b2c3d4-e5f6-7890-abcd-ef1234567890', 'store_manager1', 'hashed_password_1', 'StoreManager', '2025-09-01 10:00:00'),
('b2c3d4e5-f6a7-8901-bcde-f2345678901', 'warehouse_staff1', 'hashed_password_2', 'WarehouseStaff', '2025-09-01 10:05:00'),
('c3d4e5f6-a7b8-9012-cdef-3456789012', 'management1', 'hashed_password_3', 'Management', '2025-09-01 10:10:00'),
('d4e5f6a7-b8c9-0123-def0-4567890123', 'driver1', 'hashed_password_4', 'Driver', '2025-09-01 10:15:00'),
('e5f6a7b8-c9d0-1234-efa1-5678901234', 'assistant1', 'hashed_password_5', 'Assistant', '2025-09-01 10:20:00');

-- Insert dummy data into Customers table (unchanged)
INSERT INTO customers (customer_id, customer_name, phone_number, address) VALUES
('f6a7b8c9-d0e1-2345-fab2-6789012345', 'John Perera', '0712345678', '123 Main St, Colombo'),
('a7b8c9d0-e1f2-3456-abc3-7890123456', 'Ama Silva', '0712345679', '456 Beach Rd, Galle'),
('b8c9d0e1-f2a3-4567-bcd4-8901234567', 'Kamal Fernando', '0712345680', '789 Hill St, Kandy');
-- Insert dummy data into Cities table (exactly 25 cities in Sri Lanka)
INSERT INTO cities (city_id, city_name, province) VALUES
('c1d2e3f4-a5b6-7890-cdef-1234567890', 'Colombo', 'Western'),
('c2d3e4f5-b6c7-8901-def0-2345678901', 'Dehiwala-Mount Lavinia', 'Western'),
('c3d4e5f6-c7d8-9012-ef01-3456789012', 'Moratuwa', 'Western'),
('c4d5e6f7-d8e9-0123-f012-4567890123', 'Negombo', 'Western'),
('c5d6e7f8-e9f0-1234-0123-5678901234', 'Kandy', 'Central'),
('c6d7e8f9-f0a1-2345-1234-6789012345', 'Sri Jayawardenepura Kotte', 'Western'),
('c7d8e9f0-a1b2-3456-2345-7890123456', 'Galle', 'Southern'),
('c8d9e0f1-b2c3-4567-3456-8901234567', 'Jaffna', 'Northern'),
('c9d0e1f2-c3d4-5678-4567-9012345678', 'Trincomalee', 'Eastern'),
('d0e1f2a3-d4e5-6789-5678-0123456789', 'Gampaha', 'Western'),
('d1e2f3a4-e5f6-7890-6789-1234567890', 'Kalutara', 'Western'),
('d2e3f4a5-f6a7-8901-7890-2345678901', 'Vavuniya', 'Northern'),
('d3e4f5a6-a7b8-9012-8901-3456789012', 'Matara', 'Southern'),
('d4e5f6a7-b8c9-0123-9012-4567890123', 'Dambulla', 'Central'),
('d5e6f7a8-c9d0-1234-0123-5678901234', 'Anuradhapura', 'North Central'),
('d6e7f8a9-d0e1-2345-1234-6789012345', 'Batticaloa', 'Eastern'),
('d7e8f9a0-e1f2-3456-2345-7890123456', 'Badulla', 'Uva'),
('d8e9f0a1-f2a3-4567-3456-8901234567', 'Kurunegala', 'North Western'),
('d9e0f1a2-a3b4-5678-4567-9012345678', 'Ratnapura', 'Sabaragamuwa'),
('e0f1a2b3-b4c5-6789-5678-0123456789', 'Chilaw', 'North Western'),
('e1f2a3b4-c5d6-7890-6789-1234567890', 'Polonnaruwa', 'North Central'),
('e2f3a4b5-d6e7-8901-7890-2345678901', 'Hambantota', 'Southern'),
('e3f4a5b6-e7f8-9012-8901-3456789012', 'Mannar', 'Northern'),
('e4f5a6b7-f8a9-0123-9012-4567890123', 'Puttalam', 'North Western'),
('e5f6a7b8-a9b0-1234-0123-5678901234', 'Monaragala', 'Uva');

-- Insert dummy data into RailwayStations table (145 real stations in Sri Lanka, assigned to cities)
INSERT INTO railway_stations (station_id, station_name, city_id) VALUES
('s1a2b3c4-d5e6-7890-abcd-1234567890', 'Colombo Fort', 'c1d2e3f4-a5b6-7890-cdef-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-2345678901', 'Maradana', 'c1d2e3f4-a5b6-7890-cdef-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-3456789012', 'Dematagoda', 'c1d2e3f4-a5b6-7890-cdef-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-4567890123', 'Kelani Valley Junction', 'c1d2e3f4-a5b6-7890-cdef-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-5678901234', 'Fort', 'c1d2e3f4-a5b6-7890-cdef-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-6789012345', 'Dehiwala', 'c2d3e4f5-b6c7-8901-def0-2345678901'),
('s1a2b3c4-d5e6-7890-abcd-7890123456', 'Mount Lavinia', 'c2d3e4f5-b6c7-8901-def0-2345678901'),
('s1a2b3c4-d5e6-7890-abcd-8901234567', 'Moratuwa', 'c3d4e5f6-c7d8-9012-ef01-3456789012'),
('s1a2b3c4-d5e6-7890-abcd-9012345678', 'Panadura', 'c4d5e6f7-d8e9-0123-f012-4567890123'),
('s1a2b3c4-d5e6-7890-abcd-0123456789', 'Kalutara South', 'c4d5e6f7-d8e9-0123-f012-4567890123'),
('s1a2b3c4-d5e6-7890-abcd-1234567891', 'Aluthgama', 'c4d5e6f7-d8e9-0123-f012-4567890123'),
('s1a2b3c4-d5e6-7890-abcd-2345678902', 'Bentota', 'c4d5e6f7-d8e9-0123-f012-4567890123'),
('s1a2b3c4-d5e6-7890-abcd-3456789013', 'Kosgoda', 'c4d5e6f7-d8e9-0123-f012-4567890123'),
('s1a2b3c4-d5e6-7890-abcd-4567890124', 'Balapitiya', 'c4d5e6f7-d8e9-0123-f012-4567890123'),
('s1a2b3c4-d5e6-7890-abcd-5678901235', 'Ambalangoda', 'c4d5e6f7-d8e9-0123-f012-4567890123'),
('s1a2b3c4-d5e6-7890-abcd-6789012346', 'Hikkaduwa', 'c4d5e6f7-d8e9-0123-f012-4567890123'),
('s1a2b3c4-d5e6-7890-abcd-7890123457', 'Galle', 'c7d8e9f0-a1b2-3456-2345-7890123456'),
('s1a2b3c4-d5e6-7890-abcd-8901234568', 'Ahangama', 'c7d8e9f0-a1b2-3456-2345-7890123456'),
('s1a2b3c4-d5e6-7890-abcd-9012345679', 'Weligama', 'c7d8e9f0-a1b2-3456-2345-7890123456'),
('s1a2b3c4-d5e6-7890-abcd-0123456790', 'Matara', 'd3e4f5a6-a7b8-9012-8901-3456789012'),
('s1a2b3c4-d5e6-7890-abcd-1234567901', 'Beliatta', 'd3e4f5a6-a7b8-9012-8901-3456789012'),
('s1a2b3c4-d5e6-7890-abcd-2345678912', 'Hambantota', 'e2f3a4b5-d6e7-8901-7890-2345678901'),
('s1a2b3c4-d5e6-7890-abcd-3456789123', 'Weerawila', 'e2f3a4b5-d6e7-8901-7890-2345678901'),
('s1a2b3c4-d5e6-7890-abcd-4567891234', 'Tissamaharama', 'e2f3a4b5-d6e7-8901-7890-2345678901'),
('s1a2b3c4-d5e6-7890-abcd-5678912345', 'Gampaha', 'd0e1f2a3-d4e5-6789-5678-0123456789'),
('s1a2b3c4-d5e6-7890-abcd-6789123456', 'Negombo', 'c4d5e6f7-d8e9-0123-f012-4567890123'),
('s1a2b3c4-d5e6-7890-abcd-7891234567', 'Chilaw', 'e0f1a2b3-b4c5-6789-5678-0123456789'),
('s1a2b3c4-d5e6-7890-abcd-8902345678', 'Puttalam', 'e4f5a6b7-f8a9-0123-9012-4567890123'),
('s1a2b3c4-d5e6-7890-abcd-9013456789', 'Anuradhapura', 'd5e6f7a8-c9d0-1234-0123-5678901234'),
('s1a2b3c4-d5e6-7890-abcd-0124567890', 'Mihintale', 'd5e6f7a8-c9d0-1234-0123-5678901234'),
('s1a2b3c4-d5e6-7890-abcd-1235678901', 'Polgahawela', 'd5e6f7a8-c9d0-1234-0123-5678901234'),
('s1a2b3c4-d5e6-7890-abcd-2346789012', 'Kurunegala', 'd8e9f0a1-f2a3-4567-3456-8901234567'),
('s1a2b3c4-d5e6-7890-abcd-3457890123', 'Kuliyapitiya', 'd8e9f0a1-f2a3-4567-3456-8901234567'),
('s1a2b3c4-d5e6-7890-abcd-4568901234', 'Madhu', 'e3f4a5b6-e7f8-9012-8901-3456789012'),
('s1a2b3c4-d5e6-7890-abcd-5679012345', 'Mannar', 'e3f4a5b6-e7f8-9012-8901-3456789012'),
('s1a2b3c4-d5e6-7890-abcd-6780123456', 'Medawachchiya', 'd5e6f7a8-c9d0-1234-0123-5678901234'),
('s1a2b3c4-d5e6-7890-abcd-7891234568', 'Vavuniya', 'd2e3f4a5-f6a7-8901-7890-2345678901'),
('s1a2b3c4-d5e6-7890-abcd-8902345679', 'Kankesanthurai', 'c8d9e0f1-b2c3-4567-3456-8901234567'),
('s1a2b3c4-d5e6-7890-abcd-9013456000', 'Jaffna', 'c8d9e0f1-b2c3-4567-3456-8901234567'),
('s1a2b3c4-d5e6-7890-abcd-0124567900', 'Kankesapuri', 'c8d9e0f1-b2c3-4567-3456-8901234567'),
('s1a2b3c4-d5e6-7890-abcd-1235679012', 'Batticaloa', 'd6e7f8a9-d0e1-2345-1234-6789012345'),
('s1a2b3c4-d5e6-7890-abcd-2346789123', 'Trincomalee', 'c9d0e1f2-c3d4-5678-4567-9012345678'),
('s1a2b3c4-d5e6-7890-abcd-3457890234', 'Polonnaruwa', 'e1f2a3b4-c5d6-7890-6789-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-4568901345', 'Habarana', 'e1f2a3b4-c5d6-7890-6789-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-5679012456', 'Gal Oya Junction', 'c9d0e1f2-c3d4-5678-4567-9012345678'),
('s1a2b3c4-d5e6-7890-abcd-6780123567', 'Kandy', 'c5d6e7f8-e9f0-1234-0123-5678901234'),
('s1a2b3c4-d5e6-7890-abcd-7891234678', 'Peradeniya Junction', 'c5d6e7f8-e9f0-1234-0123-5678901234'),
('s1a2b3c4-d5e6-7890-abcd-8902345789', 'Gampola', 'c5d6e7f8-e9f0-1234-0123-5678901234'),
('s1a2b3c4-d5e6-7890-abcd-9013456900', 'Nawalapitiya', 'c5d6e7f8-e9f0-1234-0123-5678901234'),
('s1a2b3c4-d5e6-7890-abcd-0124567911', 'Hatton', 'c5d6e7f8-e9f0-1234-0123-5678901234'),
('s1a2b3c4-d5e6-7890-abcd-1235678023', 'Galboda', 'c5d6e7f8-e9f0-1234-0123-5678901234'),
('s1a2b3c4-d5e6-7890-abcd-2346789134', 'Watawala', 'c5d6e7f8-e9f0-1234-0123-5678901234'),
('s1a2b3c4-d5e6-7890-abcd-3457890245', 'Radella', 'c5d6e7f8-e9f0-1234-0123-5678901234'),
('s1a2b3c4-d5e6-7890-abcd-4568901356', 'Pattipola', 'c5d6e7f8-e9f0-1234-0123-5678901234'),
('s1a2b3c4-d5e6-7890-abcd-5679012467', 'Ohiya', 'c5d6e7f8-e9f0-1234-0123-5678901234'),
('s1a2b3c4-d5e6-7890-abcd-6780123578', 'Marathon', 'c5d6e7f8-e9f0-1234-0123-5678901234'),
('s1a2b3c4-d5e6-7890-abcd-7891234689', 'Haputale', 'c5d6e7f8-e9f0-1234-0123-5678901234'),
('s1a2b3c4-d5e6-7890-abcd-8902345900', 'Bandarawela', 'd7e8f9a0-e1f2-3456-2345-7890123456'),
('s1a2b3c4-d5e6-7890-abcd-9013456011', 'Badulla', 'd7e8f9a0-e1f2-3456-2345-7890123456'),
('s1a2b3c4-d5e6-7890-abcd-0124567122', 'Mahiyanganaya', 'd7e8f9a0-e1f2-3456-2345-7890123456'),
('s1a2b3c4-d5e6-7890-abcd-1235678234', 'Monaragala', 'e5f6a7b8-a9b0-1234-0123-5678901234'),
('s1a2b3c4-d5e6-7890-abcd-2346789345', 'Ratnapura', 'd9e0f1a2-a3b4-5678-4567-9012345678'),
('s1a2b3c4-d5e6-7890-abcd-3457890456', 'Pelmadulla', 'd9e0f1a2-a3b4-5678-4567-9012345678'),
('s1a2b3c4-d5e6-7890-abcd-4568901567', 'Dambulla', 'd4e5f6a7-b8c9-0123-9012-4567890123'),
('s1a2b3c4-d5e6-7890-abcd-5679012678', 'Sigiriya', 'd4e5f6a7-b8c9-0123-9012-4567890123'),
('s1a2b3c4-d5e6-7890-abcd-6780123789', 'Matale', 'c5d6e7f8-e9f0-1234-0123-5678901234'),
('s1a2b3c4-d5e6-7890-abcd-7891234900', 'Elahera', 'e1f2a3b4-c5d6-7890-6789-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-8902345111', 'Naula', 'e1f2a3b4-c5d6-7890-6789-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-9013456222', 'Wilgamuwa', 'e1f2a3b4-c5d6-7890-6789-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-0124567333', 'Galoya Junction', 'c9d0e1f2-c3d4-5678-4567-9012345678'),
('s1a2b3c4-d5e6-7890-abcd-1235678444', 'Baddagamuwa', 'c9d0e1f2-c3d4-5678-4567-9012345678'),
('s1a2b3c4-d5e6-7890-abcd-2346789555', 'Somawathiya', 'c9d0e1f2-c3d4-5678-4567-9012345678'),
('s1a2b3c4-d5e6-7890-abcd-3457890666', 'Kantalai', 'c9d0e1f2-c3d4-5678-4567-9012345678'),
('s1a2b3c4-d5e6-7890-abcd-4568901777', 'Kinniya', 'c9d0e1f2-c3d4-5678-4567-9012345678'),
('s1a2b3c4-d5e6-7890-abcd-5679012888', 'Uppuveli', 'c9d0e1f2-c3d4-5678-4567-9012345678'),
('s1a2b3c4-d5e6-7890-abcd-6780123999', 'China Bay', 'c9d0e1f2-c3d4-5678-4567-9012345678'),
('s1a2b3c4-d5e6-7890-abcd-7891234100', 'Dockyard', 'c9d0e1f2-c3d4-5678-4567-9012345678'),
('s1a2b3c4-d5e6-7890-abcd-8902345211', 'Valachchenai', 'd6e7f8a9-d0e1-2345-1234-6789012345'),
('s1a2b3c4-d5e6-7890-abcd-9013456322', 'Eravur', 'd6e7f8a9-d0e1-2345-1234-6789012345'),
('s1a2b3c4-d5e6-7890-abcd-0124567433', 'Batticaloa Junction', 'd6e7f8a9-d0e1-2345-1234-6789012345'),
('s1a2b3c4-d5e6-7890-abcd-1235678544', 'Okanda', 'd6e7f8a9-d0e1-2345-1234-6789012345'),
('s1a2b3c4-d5e6-7890-abcd-2346789655', 'Panichankerni', 'd6e7f8a9-d0e1-2345-1234-6789012345'),
('s1a2b3c4-d5e6-7890-abcd-3457890766', 'Vakarai', 'd6e7f8a9-d0e1-2345-1234-6789012345'),
('s1a2b3c4-d5e6-7890-abcd-4568901877', 'Maha Oya', 'd6e7f8a9-d0e1-2345-1234-6789012345'),
('s1a2b3c4-d5e6-7890-abcd-5679012988', 'Periyapola', 'd6e7f8a9-d0e1-2345-1234-6789012345'),
('s1a2b3c4-d5e6-7890-abcd-6780124009', 'Polonnaruwa', 'e1f2a3b4-c5d6-7890-6789-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-7891235110', 'Medirigiriya', 'e1f2a3b4-c5d6-7890-6789-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-8902345221', 'Hingurakgoda', 'e1f2a3b4-c5d6-7890-6789-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-9013456432', 'Minneriya', 'e1f2a3b4-c5d6-7890-6789-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-0124567543', 'Galdeniya', 'e1f2a3b4-c5d6-7890-6789-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-1235678654', 'Dekandiya', 'e1f2a3b4-c5d6-7890-6789-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-2346789765', 'Giritale', 'e1f2a3b4-c5d6-7890-6789-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-3457890876', 'Habarana', 'e1f2a3b4-c5d6-7890-6789-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-4568901987', 'Kanthale', 'c9d0e1f2-c3d4-5678-4567-9012345678'),
('s1a2b3c4-d5e6-7890-abcd-5679013098', 'Seruvila', 'c9d0e1f2-c3d4-5678-4567-9012345678'),
('s1a2b3c4-d5e6-7890-abcd-6780124109', 'Muttur', 'c9d0e1f2-c3d4-5678-4567-9012345678'),
('s1a2b3c4-d5e6-7890-abcd-7891235220', 'Omanthai', 'c8d9e0f1-b2c3-4567-3456-8901234567'),
('s1a2b3c4-d5e6-7890-abcd-8902345331', 'Paranthan', 'c8d9e0f1-b2c3-4567-3456-8901234567'),
('s1a2b3c4-d5e6-7890-abcd-9013456542', 'Pallai', 'c8d9e0f1-b2c3-4567-3456-8901234567'),
('s1a2b3c4-d5e6-7890-abcd-0124567653', 'Elephant Pass', 'c8d9e0f1-b2c3-4567-3456-8901234567'),
('s1a2b3c4-d5e6-7890-abcd-1235678764', 'Kodikamam', 'c8d9e0f1-b2c3-4567-3456-8901234567'),
('s1a2b3c4-d5e6-7890-abcd-2346789875', 'Madagal', 'c8d9e0f1-b2c3-4567-3456-8901234567'),
('s1a2b3c4-d5e6-7890-abcd-3457890986', 'Thandikulam', 'd2e3f4a5-f6a7-8901-7890-2345678901'),
('s1a2b3c4-d5e6-7890-abcd-4568902097', 'Murungan', 'd2e3f4a5-f6a7-8901-7890-2345678901'),
('s1a2b3c4-d5e6-7890-abcd-5679013108', 'Chemmalai', 'd2e3f4a5-f6a7-8901-7890-2345678901'),
('s1a2b3c4-d5e6-7890-abcd-6780124219', 'Nedunkerny', 'd2e3f4a5-f6a7-8901-7890-2345678901'),
('s1a2b3c4-d5e6-7890-abcd-7891235330', 'Puthukkudiyiruppu', 'd2e3f4a5-f6a7-8901-7890-2345678901'),
('s1a2b3c4-d5e6-7890-abcd-8902345441', 'Mullaitivu', 'd2e3f4a5-f6a7-8901-7890-2345678901'),
('s1a2b3c4-d5e6-7890-abcd-9013456652', 'Visuamadu', 'd2e3f4a5-f6a7-8901-7890-2345678901'),
('s1a2b3c4-d5e6-7890-abcd-0124567763', 'Kallikudi', 'd2e3f4a5-f6a7-8901-7890-2345678901'),
('s1a2b3c4-d5e6-7890-abcd-1235678874', 'Kilinochchi', 'c8d9e0f1-b2c3-4567-3456-8901234567'),
('s1a2b3c4-d5e6-7890-abcd-2346789985', 'Arviyil', 'c8d9e0f1-b2c3-4567-3456-8901234567'),
('s1a2b3c4-d5e6-7890-abcd-3457891096', 'Parappankulama', 'd5e6f7a8-c9d0-1234-0123-5678901234'),
('s1a2b3c4-d5e6-7890-abcd-4568902107', 'Habarana', 'd5e6f7a8-c9d0-1234-0123-5678901234'),
('s1a2b3c4-d5e6-7890-abcd-5679013218', 'Thanthirimale', 'd5e6f7a8-c9d0-1234-0123-5678901234'),
('s1a2b3c4-d5e6-7890-abcd-6780124329', 'Kala Oya', 'd5e6f7a8-c9d0-1234-0123-5678901234'),
('s1a2b3c4-d5e6-7890-abcd-7891235440', 'Galapitagala', 'd5e6f7a8-c9d0-1234-0123-5678901234'),
('s1a2b3c4-d5e6-7890-abcd-8902345551', 'Ruwanwella', 'd9e0f1a2-a3b4-5678-4567-9012345678'),
('s1a2b3c4-d5e6-7890-abcd-9013456762', 'Bulathkohupitiya', 'd9e0f1a2-a3b4-5678-4567-9012345678'),
('s1a2b3c4-d5e6-7890-abcd-0124567873', 'Avissawella', 'c1d2e3f4-a5b6-7890-cdef-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-1235678984', 'Padukka', 'c1d2e3f4-a5b6-7890-cdef-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-2346790095', 'Kirindiwela', 'c1d2e3f4-a5b6-7890-cdef-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-3457901106', 'Waga', 'c1d2e3f4-a5b6-7890-cdef-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-4569012217', 'Zoning', 'c1d2e3f4-a5b6-7890-cdef-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-5679123328', 'Homagama', 'c1d2e3f4-a5b6-7890-cdef-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-6780234439', 'Piliyandala', 'c1d2e3f4-a5b6-7890-cdef-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-7891345550', 'Boralesgamuwa', 'c1d2e3f4-a5b6-7890-cdef-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-8902456661', 'Angampitiya', 'c1d2e3f4-a5b6-7890-cdef-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-9013567772', 'Maharagama', 'c1d2e3f4-a5b6-7890-cdef-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-0124678883', 'Nugegoda', 'c1d2e3f4-a5b6-7890-cdef-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-1235789994', 'Rajagiriya', 'c6d7e8f9-f0a1-2345-1234-6789012345'),
('s1a2b3c4-d5e6-7890-abcd-2346910005', 'Battaramulla', 'c6d7e8f9-f0a1-2345-1234-6789012345'),
('s1a2b3c4-d5e6-7890-abcd-3458021116', 'Ethul Kotte', 'c6d7e8f9-f0a1-2345-1234-6789012345'),
('s1a2b3c4-d5e6-7890-abcd-4569132227', 'Pita Kotte', 'c6d7e8f9-f0a1-2345-1234-6789012345'),
('s1a2b3c4-d5e6-7890-abcd-5679243338', 'Pitipana', 'c6d7e8f9-f0a1-2345-1234-6789012345'),
('s1a2b3c4-d5e6-7890-abcd-6780354449', 'Biyagama', 'c6d7e8f9-f0a1-2345-1234-6789012345'),
('s1a2b3c4-d5e6-7890-abcd-7891465560', 'Wattala', 'c1d2e3f4-a5b6-7890-cdef-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-8902576671', 'Hendala', 'c1d2e3f4-a5b6-7890-cdef-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-9013687782', 'Wattala Sandalanka', 'c1d2e3f4-a5b6-7890-cdef-1234567890'),
('s1a2b3c4-d5e6-7890-abcd-0124798893', 'Ja Ela', 'd0e1f2a3-d4e5-6789-5678-0123456789'),
('s1a2b3c4-d5e6-7890-abcd-1235900004', 'Hunupitiya', 'd0e1f2a3-d4e5-6789-5678-0123456789'),
('s1a2b3c4-d5e6-7890-abcd-2347011115', 'Ragama', 'd0e1f2a3-d4e5-6789-5678-0123456789'),
('s1a2b3c4-d5e6-7890-abcd-3458122226', 'Nittambuwa', 'd0e1f2a3-d4e5-6789-5678-0123456789'),
('s1a2b3c4-d5e6-7890-abcd-4569233337', 'Weralupa', 'd0e1f2a3-d4e5-6789-5678-0123456789'),
('s1a2b3c4-d5e6-7890-abcd-5679344448', 'Gampaha', 'd0e1f2a3-d4e5-6789-5678-0123456789'),
('s1a2b3c4-d5e6-7890-abcd-6780455559', 'Walpita', 'd0e1f2a3-d4e5-6789-5678-0123456789'),
('s1a2b3c4-d5e6-7890-abcd-7891566670', 'Attanagalla', 'd0e1f2a3-d4e5-6789-5678-0123456789'),
('s1a2b3c4-d5e6-7890-abcd-8902677781', 'Radawadunna', 'd0e1f2a3-d4e5-6789-5678-0123456789'),
('s1a2b3c4-d5e6-7890-abcd-9013788892', 'Warakapola', 'd0e1f2a3-d4e5-6789-5678-0123456789'),
('s1a2b3c4-d5e6-7890-abcd-0124890003', 'Dehipe', 'd0e1f2a3-d4e5-6789-5678-0123456789'),
('s1a2b3c4-d5e6-7890-abcd-1236001114', 'Kegalla', 'd9e0f1a2-a3b4-5678-4567-9012345678'),
('s1a2b3c4-d5e6-7890-abcd-2347112225', 'Mawanella', 'd9e0f1a2-a3b4-5678-4567-9012345678'),
('s1a2b3c4-d5e6-7890-abcd-3458223336', 'Rambukkana', 'd9e0f1a2-a3b4-5678-4567-9012345678'),
('s1a2b3c4-d5e6-7890-abcd-4569334447', 'Kadugannawa', 'c5d6e7f8-e9f0-1234-0123-5678901234'),
('s1a2b3c4-d5e6-7890-abcd-5679445558', 'Peradeniya', 'c5d6e7f8-e9f0-1234-0123-5678901234');

-- Insert dummy data into Stores table (25 stores, one for each city)
INSERT INTO stores (store_id, name, telephone_number, address, contact_person, station_id) VALUES
('st1a2b3c4-d5e6-7890-abcd-1234567890', 'Colombo Central Store', '1123456700', '10 Station Rd, Colombo', 'Nimal Wijesinghe', 's1a2b3c4-d5e6-7890-abcd-1234567890'),
('st2b3c4d5-e6f7-8901-bcde-2345678901', 'Dehiwala Store', '1123456701', '20 Beach Rd, Dehiwala', 'Sunil Perera', 's1a2b3c4-d5e6-7890-abcd-6789012345'),
('st3c4d5e6-f7g8-9012-cdef-3456789012', 'Moratuwa Store', '1123456702', '30 Hill Rd, Moratuwa', 'Ruwan Jayasinghe', 's1a2b3c4-d5e6-7890-abcd-8901234567'),
('st4d5e6f7-g8h9-0123-def0-4567890123', 'Negombo Store', '3123456703', '40 Coastal Rd, Negombo', 'Lanka Weerakoon', 's1a2b3c4-d5e6-7890-abcd-1234567891'),
('st5e6f7g8-h9i0-1234-ef01-5678901234', 'Kandy Store', '8123456704', '50 Temple Rd, Kandy', 'Saman Kumara', 's1a2b3c4-d5e6-7890-abcd-6780123456'),
('st6f7g8h9-i0j1-2345-f012-6789012345', 'Sri Jayawardenepura Kotte Store', '1123456705', '60 Capital Ave, Kotte', 'Ama Silva', 's1a2b3c4-d5e6-7890-abcd-1235679012'),
('st7g8h9i0-j1k2-3456-0123-7890123456', 'Galle Store', '9123456706', '70 Fort Rd, Galle', 'Kamal Fernando', 's1a2b3c4-d5e6-7890-abcd-7890123457'),
('st8h9i0j1-k2l3-4567-1234-8901234567', 'Jaffna Store', '2123456707', '80 Northern Blvd, Jaffna', 'Ravi Fonseka', 's1a2b3c4-d5e6-7890-abcd-9012345679'),
('st9i0j1k2-l3m4-5678-2345-9012345678', 'Trincomalee Store', '2623456708', '90 Harbor St, Trincomalee', 'Nuwan Wijeratne', 's1a2b3c4-d5e6-7890-abcd-2346789123'),
('st0j1k2l3-m4n5-6789-3456-0123456789', 'Gampaha Store', '3323456709', '100 Junction Rd, Gampaha', 'Lakmal Perera', 's1a2b3c4-d5e6-7890-abcd-5678912345'),
('st1k2l3m4-n5o6-7890-4567-1234567890', 'Kalutara Store', '3823456710', '110 Southern Hwy, Kalutara', 'Mohan Dissanayake', 's1a2b3c4-d5e6-7890-abcd-0123456789'),
('st2l3m4n5-o6p7-8901-5678-2345678901', 'Vavuniya Store', '2423456711', '120 Transit Rd, Vavuniya', 'Priya Raman', 's1a2b3c4-d5e6-7890-abcd-7891234567'),
('st3m4n5o6-p7q8-9012-6789-3456789012', 'Matara Store', '4123456712', '130 Coastal Blvd, Matara', 'Thilak Senanayake', 's1a2b3c4-d5e6-7890-abcd-0123456790'),
('st4n5o6p7-q8r9-0123-7890-4567890123', 'Dambulla Store', '4923456713', '140 Cave Rd, Dambulla', 'Gayan Wickramasinghe', 's1a2b3c4-d5e6-7890-abcd-4568901234'),
('st5o6p7q8-r9s0-1234-8901-5678901234', 'Anuradhapura Store', '2523456714', '150 Ancient City Ave, Anuradhapura', 'Sita Rajapaksa', 's1a2b3c4-d5e6-7890-abcd-9013456789'),
('st6p7q8r9-s0t1-2345-9012-6789012345', 'Batticaloa Store', '6523456715', '160 Lagoon St, Batticaloa', 'Arun Kumaran', 's1a2b3c4-d5e6-7890-abcd-1235678901'),
('st7q8r9s0-t1u2-3456-0123-7890123456', 'Badulla Store', '5523456716', '170 Hill Country Rd, Badulla', 'Dilshan Herath', 's1a2b3c4-d5e6-7890-abcd-9013456011'),
('st8r9s0t1-u2v3-4567-1234-8901234567', 'Kurunegala Store', '3723456717', '180 North Western Blvd, Kurunegala', 'Nisha Fernando', 's1a2b3c4-d5e6-7890-abcd-2346789012'),
('st9s0t1u2-v3w4-5678-2345-9012345678', 'Ratnapura Store', '4523456718', '190 Gem Rd, Ratnapura', 'Rohan Silva', 's1a2b3c4-d5e6-7890-abcd-8902345678'),
('st0t1u2v3-w4x5-6789-3456-0123456789', 'Chilaw Store', '3223456719', '200 Coastal Rd, Chilaw', 'Malini Jayawardena', 's1a2b3c4-d5e6-7890-abcd-7891234567'),
('st1u2v3w4-x5y6-7890-4567-1234567890', 'Polonnaruwa Store', '2723456720', '210 Ancient Rd, Polonnaruwa', 'Vijay Kumar', 's1a2b3c4-d5e6-7890-abcd-6780123456'),
('st2v3w4x5-y6z7-8901-5678-2345678901', 'Hambantota Store', '4723456721', '220 Southern Hwy, Hambantota', 'Chandrika Bandara', 's1a2b3c4-d5e6-7890-abcd-2345678912'),
('st3w4x5y6-z7a8-9012-6789-3456789012', 'Mannar Store', '2323456722', '230 Island Rd, Mannar', 'Suresh Pillai', 's1a2b3c4-d5e6-7890-abcd-6780123456'),
('st4x5y6z7-a8b9-0123-7890-4567890123', 'Puttalam Store', '3223456723', '240 Lagoon Blvd, Puttalam', 'Geetha Alwis', 's1a2b3c4-d5e6-7890-abcd-8902345678'),
('st5y6z7a8-b9c0-1234-8901-5678901234', 'Monaragala Store', '5523456724', '250 Uva Rd, Monaragala', 'Kavindra De Silva', 's1a2b3c4-d5e6-7890-abcd-0124567333');

-- Insert dummy data into Products table (unchanged)
INSERT INTO products (product_type_id, product_name, space_consumption_rate) VALUES
('a9b0c1d2-e3f4-5678-abc5-9012345678', 'Detergent Box', 0.5),
('b0c1d2e3-f4a5-6789-bcd6-0123456789', 'Soap Bar', 0.2),
('c1d2e3f4-a5b6-7890-cde7-1234567890', 'Shampoo Bottle', 0.3);

-- Insert dummy data into Orders table (updated to reference new cities; placed 7+ days in advance of current date Sep 17, 2025)
INSERT INTO orders (order_id, customer_id, order_date, deliver_address, status, deliver_city_id, full_price) VALUES
('d2e3f4a5-b6c7-8901-def8-2345678901', 'f6a7b8c9-d0e1-2345-fab2-6789012345', '2025-09-01 08:00:00', '123 Main St, Colombo', 'Placed', 'c1d2e3f4-a5b6-7890-cdef-1234567890', 1500.50),
('e3f4a5b6-c7d8-9012-efa9-3456789012', 'a7b8c9d0-e1f2-3456-abc3-7890123456', '2025-09-02 09:00:00', '456 Beach Rd, Galle', 'Placed', 'c7d8e9f0-a1b2-3456-2345-7890123456', 800.75),
('f4a5b6c7-d8e9-0123-fab0-4567890123', 'b8c9d0e1-f2a3-4567-bcd4-8901234567', '2025-09-03 10:00:00', '789 Hill St, Kandy', 'Placed', 'c5d6e7f8-e9f0-1234-0123-5678901234', 2000.00);

-- Insert dummy data into OrderItems table (updated to reference new stores)
INSERT INTO order_items (item_id, order_id, store_id, product_type_id, quantity, item_price) VALUES
('a5b6c7d8-e9f0-1234-abc1-5678901234', 'd2e3f4a5-b6c7-8901-def8-2345678901', 'st1a2b3c4-d5e6-7890-abcd-1234567890', 'a9b0c1d2-e3f4-5678-abc5-9012345678', 10, 100.00),
('b6c7d8e9-f0a1-2345-bcd2-6789012345', 'd2e3f4a5-b6c7-8901-def8-2345678901', 'st1a2b3c4-d5e6-7890-abcd-1234567890', 'b0c1d2e3-f4a5-6789-bcd6-0123456789', 20, 25.50),
('c7d8e9f0-a1b2-3456-cde3-7890123456', 'e3f4a5b6-c7d8-9012-efa9-3456789012', 'st7g8h9i0-j1k2-3456-0123-7890123456', 'c1d2e3f4-a5b6-7890-cde7-1234567890', 15, 30.75);

-- Insert dummy data into Routes table (expanded to reference new cities and stores)
INSERT INTO routes (route_id, store_id, start_city_id, end_city_id, distance) VALUES
('d8e9f0a1-b2c3-4567-def4-8901234567', 'st1a2b3c4-d5e6-7890-abcd-1234567890', 'c1d2e3f4-a5b6-7890-cdef-1234567890', 'c5d6e7f8-e9f0-1234-0123-5678901234', 120),
('e9f0a1b2-c3d4-5678-efa5-9012345678', 'st7g8h9i0-j1k2-3456-0123-7890123456', 'c5d6e7f8-e9f0-1234-0123-5678901234', 'c7d8e9f0-a1b2-3456-2345-7890123456', 150),
('f0a1b2c3-d4e5-6789-fab6-0123456789', 'st8h9i0j1-k2l3-4567-1234-8901234567', 'c1d2e3f4-a5b6-7890-cdef-1234567890', 'c8d9e0f1-b2c3-4567-3456-8901234567', 200),
('g1b2c3d4-e5f6-7890-abcd-1234567891', 'st9i0j1k2-l3m4-5678-2345-9012345678', 'c1d2e3f4-a5b6-7890-cdef-1234567890', 'c9d0e1f2-c3d4-5678-4567-9012345678', 180),
('h2c3d4e5-f6g7-8901-bcde-2345678902', 'st0j1k2l3-m4n5-6789-3456-0123456789', 'c5d6e7f8-e9f0-1234-0123-5678901234', 'd0e1f2a3-d4e5-6789-5678-0123456789', 90);

-- Insert dummy data into RouteOrders table (unchanged)
INSERT INTO route_orders (route_order_id, route_id, order_id) VALUES
('a1b2c3d4-e5f6-7890-abc7-1234567890', 'd8e9f0a1-b2c3-4567-def4-8901234567', 'd2e3f4a5-b6c7-8901-def8-2345678901'),
('b2c3d4e5-f6a7-8901-bcd8-2345678901', 'e9f0a1b2-c3d4-5678-efa5-9012345678', 'e3f4a5b6-c7d8-9012-efa9-3456789012'),
('c3d4e5f6-a7b8-9012-cde9-3456789012', 'f0a1b2c3-d4e5-6789-fab6-0123456789', 'f4a5b6c7-d8e9-0123-fab0-4567890123');

-- Insert dummy data into Trains table (exactly 20 trains, based on real Sri Lanka named trains)
INSERT INTO trains (train_id, train_name, capacity) VALUES
('t1a2b3c4-d5e6-7890-abcd-1234567890', 'Udarata Menike', 1000),
('t2b3c4d5-e6f7-8901-bcde-2345678901', 'Raja Rata Rajina', 1200),
('t3c4d5e6-f7g8-9012-cdef-3456789012', 'Samanala', 800),
('t4d5e6f7-g8h9-0123-def0-4567890123', 'Podi Menike', 900),
('t5e6f7g8-h9i0-1234-ef01-5678901234', 'Yal Devi', 1100),
('t6f7g8h9-i0j1-2345-f012-6789012345', 'Uttara Devi', 950),
('t7g8h9i0-j1k2-3456-0123-7890123456', 'Night Mail', 1300),
('t8h9i0j1-k2l3-4567-1234-8901234567', 'Intercity 1', 1050),
('t9i0j1k2-l3m4-5678-2345-9012345678', 'Intercity 2', 1150),
('t0j1k2l3-m4n5-6789-3456-0123456789', 'Coastal Express', 850),
('t1k2l3m4-n5o6-7890-4567-1234567890', 'Southern Express', 1000),
('t2l3m4n5-o6p7-8901-5678-2345678901', 'Cargo Freight 1', 1500),
('t3m4n5o6-p7q8-9012-6789-3456789012', 'Cargo Freight 2', 1400),
('t4n5o6p7-q8r9-0123-7890-4567890123', 'Tea Country Special', 700),
('t5o6p7q8-r9s0-1234-8901-5678901234', 'Northern Link', 1100),
('t6p7q8r9-s0t1-2345-9012-6789012345', 'Eastern Cargo', 1200),
('t7q8r9s0-t1u2-3456-0123-7890123456', 'Central Freight', 1300),
('t8r9s0t1-u2v3-4567-1234-8901234567', 'Southern Cargo', 1250),
('t9s0t1u2-v3w4-5678-2345-9012345678', 'Western Express', 950),
('t0t1u2v3-w4x5-6789-3456-0123456789', 'Island Freight', 1600);

-- Insert dummy data into TrainSchedules table (expanded to reference new trains and stations; dates after Sep 17, 2025)
INSERT INTO train_schedules (schedule_id, train_id, station_id, scheduled_date, departure_time, arrival_time, status) VALUES
('f6a7b8c9-d0e1-2345-fab2-6789012345', 't1a2b3c4-d5e6-7890-abcd-1234567890', 's1a2b3c4-d5e6-7890-abcd-1234567890', '2025-09-25', '08:00:00', '12:00:00', 'Planned'),
('a7b8c9d0-e1f2-3456-abc3-7890123456', 't2b3c4d5-e6f7-8901-bcde-2345678901', 's1a2b3c4-d5e6-7890-abcd-6789012345', '2025-09-26', '09:00:00', '13:30:00', 'Planned'),
('b8c9d0e1-f2a3-4567-bcd4-8901234567', 't3c4d5e6-f7g8-9012-cdef-3456789012', 's1a2b3c4-d5e6-7890-abcd-7890123457', '2025-09-27', '07:30:00', '11:45:00', 'Planned'),
('c9d0e1f2-a3b4-5678-cde5-9012345678', 't4d5e6f7-g8h9-0123-def0-4567890123', 's1a2b3c4-d5e6-7890-abcd-9012345679', '2025-09-28', '10:00:00', '14:00:00', 'Planned');

-- Insert dummy data into RailAllocations table (unchanged)
INSERT INTO rail_allocations (allocation_id, order_id, schedule_id, shipment_date, status) VALUES
('b8c9d0e1-f2a3-4567-bcd4-8901234567', 'd2e3f4a5-b6c7-8901-def8-2345678901', 'f6a7b8c9-d0e1-2345-fab2-6789012345', '2025-09-25', 'Planned'),
('c9d0e1f2-a3b4-5678-cde5-9012345678', 'e3f4a5b6-c7d8-9012-efa9-3456789012', 'a7b8c9d0-e1f2-3456-abc3-7890123456', '2025-09-26', 'Planned');

-- Insert dummy data into Drivers table (unchanged)
INSERT INTO drivers (driver_id, name, weekly_working_hours, user_id) VALUES
('d0e1f2a3-b4c5-6789-def6-0123456789', 'Saman Kumara', 20, 'd4e5f6a7-b8c9-0123-def0-4567890123'),
('e1f2a3b4-c5d6-7890-efa7-1234567890', 'Ravi Fonseka', 15, 'd4e5f6a7-b8c9-0123-def0-4567890123');

-- Insert dummy data into Assistants table (unchanged)
INSERT INTO assistants (assistant_id, name, weekly_working_hours, user_id) VALUES
('f2a3b4c5-d6e7-8901-fab8-2345678901', 'Nuwan Wijeratne', 30, 'e5f6a7b8-c9d0-1234-efa1-5678901234'),
('a3b4c5d6-e7f8-9012-abc9-3456789012', 'Lakmal Perera', 25, 'e5f6a7b8-c9d0-1234-efa1-5678901234');

-- Insert dummy data into Trucks table (unchanged)
INSERT INTO trucks (truck_id, license_num, capacity, is_active) VALUES
('b4c5d6e7-f8a9-0123-bcd0-4567890123', 'WP-1234', 500, TRUE),
('c5d6e7f8-a9b0-1234-cde1-5678901234', 'SP-5678', 750, TRUE);

-- Insert dummy data into TruckSchedules table (updated dates after Sep 17, 2025; reference new routes)
INSERT INTO truck_schedules (schedule_id, route_id, truck_id, driver_id, assistant_id, scheduled_date, departure_time, duration, status) VALUES
('d6e7f8a9-b0c1-2345-def2-6789012345', 'd8e9f0a1-b2c3-4567-def4-8901234567', 'b4c5d6e7-f8a9-0123-bcd0-4567890123', 'd0e1f2a3-b4c5-6789-def6-0123456789', 'f2a3b4c5-d6e7-8901-fab8-2345678901', '2025-09-20', '08:00:00', 4, 'Planned'),
('e7f8a9b0-c1d2-3456-efa3-7890123456', 'e9f0a1b2-c3d4-5678-efa5-9012345678', 'c5d6e7f8-a9b0-1234-cde1-5678901234', 'e1f2a3b4-c5d6-7890-efa7-1234567890', 'a3b4c5d6-e7f8-9012-abc9-3456789012', '2025-09-21', '09:00:00', 5, 'Planned');

-- Insert dummy data into TruckAllocations table (updated dates)
INSERT INTO truck_allocations (allocation_id, order_id, schedule_id, shipment_date, status) VALUES
('f8a9b0c1-d2e3-4567-fab4-8901234567', 'd2e3f4a5-b6c7-8901-def8-2345678901', 'd6e7f8a9-b0c1-2345-def2-6789012345', '2025-09-20', 'Planned'),
('a9b0c1d2-e3f4-5678-abc5-9012345678', 'e3f4a5b6-c7d8-9012-efa9-3456789012', 'e7f8a9b0-c1d2-3456-efa3-7890123456', '2025-09-21', 'Planned');