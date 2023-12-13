df = pandas.read_csv('https://raw.githubusercontent.com/kahyuwesuma/global-air-pollution/main/global%20air%20pollution%20dataset.csv')

def display_dataframe(df):   
    return df.describe()

def display_cluster_info(cluster_info_data):
    st.title("Cluster Description")

    # Sidebar dengan pilihan cluster
    selected_cluster = st.sidebar.selectbox("Pilih Cluster", list(cluster_info_data.keys()))

    # Menampilkan hasil describe DataFrame
    st.subheader("Statistik Deskriptif Data")
    df_describe = display_dataframe(df)  
    st.dataframe(df_describe)

    # Menampilkan informasi pada bagian utama halaman
    st.subheader(selected_cluster)
    st.write(f"**Deskripsi:** {cluster_info_data[selected_cluster]['Description']}")

if __name__ == "__main__":
    display_cluster_info(cluster_info_data)
