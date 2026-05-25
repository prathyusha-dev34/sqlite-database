import { useEffect, useState } from "react";
import API from "./api";

function App() {

  const [movies, setMovies] = useState([]);

  const [formData, setFormData] = useState({
    title: "",
    genre: "",
    rating: "",
    image: "",
  });

  // Fetch Movies
  const fetchMovies = async () => {

    try {

      const response = await API.get("/movies");

      setMovies(response.data);

    } catch (error) {

      console.log(error);
    }
  };

  useEffect(() => {
    fetchMovies();
  }, []);

  // Handle Input
  const handleChange = (e) => {

    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  // Add Movie
  const addMovie = async (e) => {

    e.preventDefault();

    try {

      await API.post("/movies", formData);

      alert("Movie Added");

      fetchMovies();

    } catch (error) {

      console.log(error);
    }
  };

  // Delete Movie
  const deleteMovie = async (id) => {

    try {

      await API.delete(`/movies/${id}`);

      fetchMovies();

    } catch (error) {

      console.log(error);
    }
  };

  return (

    <div style={{ textAlign: "center" }}>

      <h1>🎬 Movie App</h1>

      {/* Add Movie */}

      <h2>Add Movie</h2>

      <form onSubmit={addMovie}>

        <input
          type="text"
          name="title"
          placeholder="Movie Title"
          onChange={handleChange}
        />

        <input
          type="text"
          name="genre"
          placeholder="Genre"
          onChange={handleChange}
        />

        <input
          type="text"
          name="rating"
          placeholder="Rating"
          onChange={handleChange}
        />

        <input
          type="text"
          name="image"
          placeholder="Image URL"
          onChange={handleChange}
        />

        <button type="submit">
          Add Movie
        </button>

      </form>

      <hr />

      {/* Movie List */}

      <div>

        {movies.map((movie) => (

          <div
            key={movie.id}
            style={{
              border: "1px solid gray",
              padding: "10px",
              margin: "20px",
            }}
          >

            <img
              src={movie.image}
              alt={movie.title}
              width="200"
            />

            <h2>{movie.title}</h2>

            <p>{movie.genre}</p>

            <p>{movie.rating}</p>

            <button
              onClick={() => deleteMovie(movie.id)}
            >
              Delete
            </button>

          </div>
        ))}

      </div>

    </div>
  );
}

export default App;