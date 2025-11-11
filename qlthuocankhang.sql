-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th10 04, 2025 lúc 03:02 AM
-- Phiên bản máy phục vụ: 8.0.42
-- Phiên bản PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `qlthuocankhang`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `danhmuc`
--

CREATE TABLE `danhmuc` (
  `MaDanhMuc` int NOT NULL,
  `TenDanhMuc` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `MoTa` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `danhmuc`
--

INSERT INTO `danhmuc` (`MaDanhMuc`, `TenDanhMuc`, `MoTa`) VALUES
(1, 'Hot Sale', 'Sản phẩm giảm giá hot'),
(2, 'Thuốc', 'Các loại thuốc được phép bán'),
(3, 'Thực phẩm chức năng', 'Thực phẩm hỗ trợ sức khỏe'),
(4, 'Thiết bị, dụng cụ y tế', 'Thiết bị dùng trong y tế'),
(5, 'Dược mỹ phẩm', 'Sản phẩm chăm sóc da và sức khỏe'),
(6, 'Chăm sóc cá nhân', 'Sản phẩm vệ sinh, chăm sóc cơ thể');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `sanpham`
--

CREATE TABLE `sanpham` (
  `MaSanPham` int NOT NULL,
  `TenSanPham` varchar(200) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `DungTichHoacKhoiLuong` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `GiaGoc` decimal(15,2) DEFAULT NULL,
  `GiaKhuyenMai` decimal(15,2) DEFAULT NULL,
  `PhanTramGiam` int DEFAULT NULL,
  `DonViTinh` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `MaDanhMuc` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `sanpham`
--

INSERT INTO `sanpham` (`MaSanPham`, `TenSanPham`, `DungTichHoacKhoiLuong`, `GiaGoc`, `GiaKhuyenMai`, `PhanTramGiam`, `DonViTinh`, `MaDanhMuc`) VALUES
(1, 'Nước muối Vietrue sát khuẩn, súc miệng', '500ml', 7000.00, 4900.00, 30, 'chai', 1),
(2, 'Thực phẩm dinh dưỡng Y Học Ensure Gold', 'lon 800g', 932000.00, 845000.00, 9, 'lon', 3),
(3, 'Sữa bột Anlene Gold hương Vani', 'lon 800g', 555000.00, 480000.00, 13, 'lon', 3),
(4, 'Costar Omega 3', 'lọ 365 viên', 972000.00, 729000.00, 25, 'lọ', 3),
(5, 'Sắc Ngọc Khang', 'hộp 180 viên', 666000.00, 532800.00, 20, 'hộp', 3);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `danhmuc`
--
ALTER TABLE `danhmuc`
  ADD PRIMARY KEY (`MaDanhMuc`);

--
-- Chỉ mục cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  ADD PRIMARY KEY (`MaSanPham`),
  ADD KEY `MaDanhMuc` (`MaDanhMuc`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `danhmuc`
--
ALTER TABLE `danhmuc`
  MODIFY `MaDanhMuc` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  MODIFY `MaSanPham` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  ADD CONSTRAINT `sanpham_ibfk_1` FOREIGN KEY (`MaDanhMuc`) REFERENCES `danhmuc` (`MaDanhMuc`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
